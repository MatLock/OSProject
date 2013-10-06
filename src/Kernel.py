'''
Created on 30/09/2013

@author: matlock
'''
import Queue
import threading
from SortedQueue import *
from Instruction import *
from Program import *
from Algorithm import *


kernel_semaphore = threading.Semaphore(1)
cpu_semaphore = threading.Semaphore(0)

class Kernel(threading.Thread):
    
    def __init__(self,scheduler,cpu,ioQueue,pcb):
        threading.Thread.__init__(self)
        self.scheduler = scheduler
        self.cpu = cpu
        self.ioQueue = ioQueue
        self.pcb = pcb
        
    def execute(self,program):
        self.pcb.setInstruction(program.getIndex())
        self.pcb.setProgram(program)
        cpu_semaphore.release()
        
    def run(self):
        while(True):
            kernel_semaphore.acquire()
            self.execute(self.scheduler.get())
            print "KERNEL: Getting a program !!"
            cpu_semaphore.release()
            
class Pcb():
    
    def __init__(self):
        self.instruction = None
        self.program = None
        
    def setInstruction(self,aNumberOfInstruction):
        self.instruction = aNumberOfInstruction
        
    def setProgram(self,aProgram):
        self.program = aProgram
        
    def getProgram(self):
        return self.program
    
    def getInstruction(self):
        return self.instruction
            
        
class Scheduler(threading.Thread):
    
    def __init__(self,algorithm):
        self.algorithm = algorithm
        
    def add(self,program):
        self.algorithm.add(program)
        
    def get(self):
        return self.algorithm.get()
    
    def isEmpty(self):
        return self.algorithm.isEmpty()
    
class CPU(threading.Thread):
    
    def __init__(self,kernel,scheduler,ioqueue,pcb):
        threading.Thread.__init__(self)
        self.kernel = kernel
        self.ioqueue = ioqueue
        self.scheduler = scheduler
        self.state = Idle()
        self.pcb = pcb
        
    def setKernel(self,kernel):
        self.kernel = kernel
    
    def changeState(self):
        self.state.changeState(self)
    
    def execute(self):
        self.state.execute(self)
        
    def run(self):
        while(True):
            cpu_semaphore.acquire()
            self.execute()
            
    def setPCB(self,pcb):
        self.pcb = pcb
        
    def executeBasicInstruction(self):
        print "CPU : Running a Basic instruction of the program: " + str(self.pcb.getProgram().getIdentifier())
        time.sleep(3)
        
    def executeIOinstruction(self):
        print "CPU : I/O instruction of the program: "+"'"+str(self.pcb.getProgram().getIdentifier())+"'"+" Detected"
        self.ioqueue.put(self.pcb.getProgram())
        io_semaphore.release()
        
class Idle(): 
    
    def changeState(self,cpu):
        print "CPU:  Changing to busy state.. "
        cpu.state = Busy()
        
    def execute(self, cpu):
        cpu_semaphore.acquire()
        cpu.changeState()
        i = cpu.pcb.getInstruction()
        while (i <  cpu.pcb.getProgram().size):
            x = cpu.pcb.getProgram().getInstruction(i)
            if (not x.io()):
                x.execute(cpu) 
                i += 1
                cpu.pcb.getProgram().setIndex(i)
            else:
                x.execute(cpu)
                break
        cpu.changeState()
        kernel_semaphore.release()
        
        
class Busy():
    
    def changeState(self,cpu):
        print "CPU: Changing to idle state.. "
        cpu.state = Idle()
    
    def execute(self,program,cpu):
        cpu.scheduler.add(program)
        

def main():
    instruction1 = BasicInstruction()
    instruction2 = BasicInstruction()
    ioInstruction = IO_Instruction()
    program = Program(0,'a',False)
    program.addInstruction(instruction1)
    program.addInstruction(ioInstruction)
    program.addInstruction(instruction2)
    program2 = Program(0,'b',False)
    program2.addInstruction(instruction1)
    program2.addInstruction(instruction1)
    ioqueue = IOQueue(None)
    pcb = Pcb()
    scheduler = Scheduler(FIFO())
    scheduler.add(program)
    scheduler.add(program2)
    cpu = CPU(None,scheduler,ioqueue,pcb)
    kernel = Kernel(scheduler,cpu,ioqueue,pcb)
    ioqueue.setScheduler(scheduler)
    cpu.setKernel(kernel)
    cpu.start()
    ioqueue.start()
    kernel.start()
    
if __name__ == '__main__':

    main()
    
    