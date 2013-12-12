'''
Created on 07/10/2013

@author: matlock,santiago
'''


from src.Timer import Timer
from src.Logger import *
from src.Frame import Frame
from src.CPU  import *
from src.SortedQueue import *
from src.Program import Program
from src.Scheduler import Scheduler
from src.PCB import PCB
from src.Memory import Memory 
from src.Disk import Disk
from src.Instruction import BasicInstruction
from src.Instruction import IO_Instruction
from src.Instruction import Priority_Instruction
from src.MMU import MMU
from src.Algorithm  import PFIFO

class Kernel(threading.Thread):
    
    def __init__(self,cpu,ioqueue,scheduler,mmu,disk,logger):
        threading.Thread.__init__(self)
        self.cpu = cpu
        self.ioqueue = ioqueue
        self.scheduler = scheduler
        self.mmu = mmu
        self.disk = disk
        self.logger = logger
        
    def getDisk(self):
        return self.disk
    
    def getLogger(self):
        return self.logger
        
    def getMMU(self):
        return self.mmu
      
    def getCPU(self):
        return self.cpu
    
    def getIOqueue(self):
        return self.ioqueue
    
    def getScheduler(self):
        return self.scheduler
    
    def shutDown(self):
        self.getLogger().write("KERNEL: ShutDown! \n")
        
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
            size = program.size()
            base = self.mmu.getBase(size)
            pcb = PCB(pid,priority,base,size)
            self.mmu.load(pcb,program,base)
            self.scheduler.add(pcb)
        except (Exception):
            try:
                self.mmu.compact()
                base = self.mmu.getBase(size)
                pcb = PCB(pid,priority,base,size)
                self.mmu.load(pcb,program,base)
                self.scheduler.add(pcb)
            except (Exception):
                self.getDisk().save(program)
                
    def saveOnDisk(self,aList):
        for i in aList:
            self.getDisk().save(i)
        
        
    def sendToIO(self,pcb):
        self.getLogger().write("KERNEL: Sending program  " +str(pcb.getPid())+ "  to IOQueue!! \n")
        self.getIOqueue().put(pcb)
        io_semaphore.release()
        
    def savePCB(self,pcb):
        self.getScheduler().add(pcb)
        
    def execute(self):
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
            
    def stateOfCpu(self):
        return self.getCPU().printState()
            
    def delete(self,pid):
        self.getMMU().delete(pid)
        size = len(self.getMMU().getMemory().getEmptyCells())
        if ((not self.getDisk().isEmpty()) and self.getDisk().existProgramWithSizeMinorTo(size)):
            program = self.getDisk().get(size)
            self.saveProgram(program)
            
    def executeProgram(self,anIdentifier):
        program = self.getDisk().getProgram(anIdentifier)
        self.saveProgram(program)
        self.start()
        self.getCPU().start()
        self.getIOqueue().start()
        
    def candidates(self):
        size = len(self.getMMU().getMemory().getEmptyCells())
        programs = self.getDisk().programList
        current = 0
        result = []
        for i in range(0,len(programs)):
            if (programs[i].size() + current <= size):
                result.append(i)
                current += programs[i].size()
        return result
    
    def executeAll(self):
        candidates = self.candidates()
        candidates.reverse()
        for i in range(0,len(candidates)):
            self.saveProgram(self.getDisk().programList.pop(i))    
        self.start()
        self.getCPU().start()
        self.getIOqueue().start()
        
    
        
            
def main0():
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
    
def main():
    instruction1 = BasicInstruction()
    instruction2 = IO_Instruction()
    instruction3 = Priority_Instruction()
    program = Program('a')
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    programd = Program('d')
    programd.addInstruction(instruction1)
    programd.addInstruction(instruction1)
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
    logger = Logger("/home/matlock/Escritorio/Sistemas Operativos/OSProyect/resource/log.txt")
    mmu = MMU(logger)
    mmu.addEmptyFrame(frame1)
    cpu = CPU(None,mmu,None,timer,logger)
    scheduler = Scheduler(PFIFO())
    ioqueue = IOQueue(scheduler,logger)
    disk = Disk(None)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk,logger)
    disk.setKernel(kernel)
    cpu.setKernel(kernel)
    x = []
    x.append(program)
    x.append(programb)
    x.append(programc)
    x.append(programd)
    kernel.saveOnDisk(x)
    kernel.executeProgram('a')
    
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
        
def main2():

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
        
        
def main1():
    instruction1 = BasicInstruction()
    instruction3 = Priority_Instruction()
    logger = Logger("../resource/log.txt")
    program = Program('a')
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
    program.addInstruction(instruction1)
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
    cpu = CPU(None,mmu,None,timer,logger)
    scheduler = Scheduler(PFIFO())
    ioqueue = IOQueue(scheduler,logger)
    disk = Disk(None)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk,logger)
    disk.setKernel(kernel)
    disk.save(program)
    disk.save(programb)
    disk.save(programc)
    cpu.setKernel(kernel)
    kernel.executeProgram('a')   
    
if __name__ == '__main__':
    main()
        