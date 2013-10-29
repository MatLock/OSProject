'''
Created on 07/10/2013

@author: matlock
'''

from Program import *
from PCB import *
from CPU import *
from Memory import *
from MMU import *
from Scheduler import *
from Algorithm import *
import threading
from SortedQueue import *
from Instruction import *
from Frame import *


class Kernel(threading.Thread):
    
    def __init__(self,cpu,ioqueue,scheduler,mmu):
        threading.Thread.__init__(self)
        self.cpu = cpu
        self.ioqueue = ioqueue
        self.scheduler = scheduler
        self.mmu = mmu
        
       
    def getCPU(self):
        return self.cpu
    
    def getIOqueue(self):
        return self.ioqueue
    
    def getScheduler(self):
        return self.scheduler
    
    def shutDown(self):
        print "KERNEL: Shutdown!!"
    
    def saveProgram(self,program):
        pid = program.getName()
        base = self.mmu.getBase()
        priority = 0 #self.addPriority()
        size = len(program.instruction)
        pcb = PCB(pid,priority,base,size)
        self.mmu.load(pcb,program)
        self.scheduler.add(pcb)
        
    def sendToIO(self,pcb):
        print "KERNEL:  Sending to IOQueue !!"
        self.getIOqueue().put(pcb)
        io_semaphore.release()
        
    def execute(self):
        print "KERNEL : Running !"
        if (self.scheduler.isEmpty() and self.ioqueue.isEmpty()):
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
            
            
def main():
    instruction1 = BasicInstruction()
    instruction2 = IO_Instruction()
    instruction3 = BasicInstruction()
    program = Program('a')
    programb = Program('b') 
    program.addInstruction(instruction1)
    program.addInstruction(instruction2)
    program.addInstruction(instruction3)
    programb.addInstruction(instruction1)
    programb.addInstruction(instruction1)
    programb.addInstruction(instruction3)
    memory = Memory()
    memory.buildMemory(6)
    frame1 = Frame(memory,0)
    frame2 = Frame(memory,3)
    mmu = MMU()
    mmu.addEmptyFrame(frame1)
    mmu.addEmptyFrame(frame2)
    cpu = CPU(None,mmu,None)
    scheduler = Scheduler(FIFO())
    ioqueue = IOQueue(scheduler)
    kernel = Kernel(cpu,ioqueue,scheduler,mmu)
    cpu.setKernel(kernel)
    kernel.saveProgram(program)
    kernel.saveProgram(programb)
    kernel.start()
    cpu.start()
    ioqueue.start()
    
if __name__ == '__main__':
    main()
        