'''
Created on 07/10/2013

@author: matlock
'''


from src.Timer import *
from src.Frame import *
from src.CPU import *
from src.Instruction import *
from src.Program import *
from src.SortedQueue import *
from src.Scheduler import *
from src.PCB import *
from src.Algorithm import *
from src.Memory import *
from src.MMU import *

class Kernel(threading.Thread):
    
    def __init__(self,cpu,ioqueue,scheduler,mmu,disk):
        threading.Thread.__init__(self)
        self.cpu = cpu
        self.ioqueue = ioqueue
        self.scheduler = scheduler
        self.mmu = mmu
        self.disk = disk
        
    def getDisk(self):
        return self.disk
        
    def getMMU(self):
        return self.mmu
      
    def getCPU(self):
        return self.cpu
    
    def getIOqueue(self):
        return self.ioqueue
    
    def getScheduler(self):
        return self.scheduler
    
    def shutDown(self):
        print ("KERNEL: ShutDown!")
        
    def containsPriorityInstruction(self,program): 
        y = filter(lambda x : isinstance(x,Priority_Instruction),program.getInstruction())
        return len(y) >= 1
            
    def addPriority(self,program):
        if(self.containsPriorityInstruction(program)):
            return 1
        else:
            return 0
        
    def saveProgram(self,program):
        try:
            pid = program.getName()
            priority = self.addPriority(program)
            size = len(program.instruction)
            base = self.mmu.getBase(size)
            pcb = PCB(pid,priority,base,size)
            self.mmu.load(pcb,program)
            self.scheduler.add(pcb)
        except (Exception):
            try:
                self.mmu.compact()
                base = self.mmu.getBase(size)
                pcb = PCB(pid,priority,base,size)
                self.mmu.load(pcb,program)
                self.scheduler.add(pcb)
            except (Exception):
                self.getDisk().save(program)
        
        
    def sendToIO(self,pcb):
        print ("KERNEL:  Sending program " + str(pcb.getPid())+ " to IOQueue !!")
        self.getIOqueue().put(pcb)
        io_semaphore.release()
        
    def savePCB(self,pcb):
        self.getScheduler().add(pcb)
        
    def execute(self):
        print ("KERNEL : Running !")
        if (self.scheduler.isEmpty() and self.ioqueue.isEmpty() and self.getDisk().isEmpty()):
            self.cpu.shutDown()
            self.ioqueue.shutDown()
            self.shutDown()
        elif (not (self.ioqueue.isEmpty()) and self.scheduler.isEmpty()):
            kernel_semaphore2.acquire()
        self.cpu.setPCB(self.scheduler.get())
        cpu_semaphore.release()
        
    def run(self):
        while(True):
            kernel_semaphore.acquire()
            self.execute()
            
    def delete(self,pid):
        sizeOfProgramDeleted = self.getMMU().delete(pid)
        if (not self.getDisk().isEmpty()):
            self.getDisk().get(sizeOfProgramDeleted)
            
    def executeProgram(self,anIdentifier):
        program = self.getDisk().getProgram(anIdentifier)
        self.saveProgram(program)
        self.start()
        self.getCPU().start()
        self.getIOqueue().start()
        
            
def main9():
    instruction1 = BasicInstruction()
    instruction2 = IO_Instruction()
    instruction3 = Priority_Instruction()
    program = Program('a')
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    programb = Program('b')
    programb.addInstruction(instruction3)
    programc = Program('c')
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    timer = Timer(2)
    memory = Memory()
    memory.buildMemory(9)
    frame1 = Frame(memory,0,9)
    mmu = MMU()
    mmu.addEmptyFrame(frame1)
    cpu = CPU(None,mmu,None,timer)
    scheduler = Scheduler(PFIFO())
    ioqueue = IOQueue(scheduler)
    disk = Disk(None)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk)
    disk.setKernel(kernel)
    cpu.setKernel(kernel)
    kernel.saveProgram(program)
    kernel.saveProgram(programb)
    kernel.saveProgram(programc)
    kernel.start()
    cpu.start()
    ioqueue.start()
    
def main4():
    instruction1 = BasicInstruction()
    instruction2 = IO_Instruction()
    instruction3 = Priority_Instruction()
    program = Program('a')
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    programd = Program('d')
    programd.addInstruction(instruction1)
    programd.addInstruction(instruction1)
    programd.addInstruction(instruction1)
    programb = Program('b')
    programb.addInstruction(instruction3)
    programc = Program('c')
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    timer = Timer(2)
    memory = Memory()
    memory.buildMemory(9)
    frame1 = Frame(memory,0,9)
    mmu = MMU()
    mmu.addEmptyFrame(frame1)
    cpu = CPU(None,mmu,None,timer)
    scheduler = Scheduler(PFIFO())
    ioqueue = IOQueue(scheduler)
    disk = Disk(None)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk)
    disk.setKernel(kernel)
    cpu.setKernel(kernel)
    kernel.saveProgram(program)
    kernel.saveProgram(programb)
    kernel.saveProgram(programc)
    kernel.saveProgram(programd)
    print(len(disk.programList))
    
def main3():
    if(1==1):
        instruction1 = BasicInstruction()
        instruction2 = BasicInstruction()      
        memory = Memory()
        memory.buildMemory(5)
        frame1 = Frame(memory,0,1)
        frame2 = Frame(memory,1,2)
        frame3 = Frame(memory,3,1)
        frame4 = Frame(memory,4,1)
        mmu = MMU()
        mmu.fullFrames.append(frame1)
        mmu.fullFrames.append(frame3)
        mmu.emptyFrames.append(frame2)
        mmu.emptyFrames.append(frame4)
        program = Program('a')
        program.addInstruction(instruction1)
        pcbA = PCB('a',0,0,1)
        programb = Program('b')
        pcbB = PCB('b',0,3,1)
        programb.addInstruction(instruction1)
        frame1.load(pcbA,program)
        frame3.load(pcbB,programb)
        programc = Program('c')
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programd = Program('d')
        programd.addInstruction(instruction2)
        programd.addInstruction(instruction2)
        programd.addInstruction(instruction2)
        scheduler = Scheduler(PFIFO())
        disk = Disk(None)
        kernel = Kernel (None,None,scheduler,mmu,disk)
        disk.setKernel(kernel)
        memory.printMemory()
        kernel.saveProgram(programc)
        print( "     ")
        memory.printMemory()
        kernel.saveProgram(programd)
        print( "     ")
        memory.printMemory()
        print(len(disk.programList))
        
def main6():

        instruction1 = BasicInstruction()
        instruction2 = BasicInstruction()      
        memory = Memory()
        memory.buildMemory(5)
        frame1 = Frame(memory,0,1)
        frame2 = Frame(memory,1,2)
        frame3 = Frame(memory,3,1)
        frame4 = Frame(memory,4,1)
        mmu = MMU()
        mmu.fullFrames.append(frame1)
        mmu.fullFrames.append(frame3)
        mmu.emptyFrames.append(frame2)
        mmu.emptyFrames.append(frame4)
        program = Program('a')
        program.addInstruction(instruction1)
        pcbA = PCB('a',0,0,1)
        programb = Program('b')
        pcbB = PCB('b',0,3,1)
        programb.addInstruction(instruction1)
        frame1.load(pcbA,program)
        frame3.load(pcbB,programb)
        memory.printMemory()
        print(memory.getEmptyCells())
        mmu.compact()
        memory.printMemory()
        
        
def main():
    instruction1 = BasicInstruction()
    instruction3 = Priority_Instruction()
    program = Program('a')
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    programb = Program('b')
    programb.addInstruction(instruction3)
    programc = Program('c')
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    programc.addInstruction(instruction1)
    timer = Timer(2)
    memory = Memory()
    memory.buildMemory(9)
    frame1 = Frame(memory,0,9)
    mmu = MMU()
    mmu.addEmptyFrame(frame1)
    cpu = CPU(None,mmu,None,timer)
    scheduler = Scheduler(PFIFO())
    ioqueue = IOQueue(scheduler)
    disk = Disk(None)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk)
    disk.setKernel(kernel)
    disk.save(program)
    cpu.setKernel(kernel)
    kernel.executeProgram('a')   
    
if __name__ == '__main__':
    main()
        