'''
Created on 30/09/2013

@author: matlock
'''
import threading
import time

  
cpu_semaphore = threading.Semaphore(0)   
kernel_semaphore = threading.Semaphore(1)    
    
class CPU(threading.Thread):
    
    def __init__(self,kernel,mmu,pcb):
        threading.Thread.__init__(self)
        self.state = Idle()
        self.kernel = kernel
        self.mmu = mmu
        self.pcb = pcb
        
    def getMMU(self):
        return self.mmu
        
    def setKernel(self,kernel):
        self.kernel = kernel
    
    def changeState(self):
        self.state.changeState(self)
        
    def getPCB(self):
        return self.pcb
            
    def setPCB(self,pcb):
        self.pcb = pcb
        
    def execute(self):
        self.state.execute(self)
        
    def executeIOinstruction(self):
        self.kernel.sendToIO(self.pcb)
        
    def executeBasicInstruction(self):
        print "CPU: Running a basic instruction of the program:   " + str(self.getPCB().getPid())
        
    def shutDown(self):
        print "CPU: Shutdown!! "
    
    def run(self):
        while(True):
            cpu_semaphore.acquire()
            self.execute()
        
class Idle(): 
    
    def changeState(self,cpu):
        print "CPU:  Changing to busy state.. "
        cpu.state = Busy()
    
    def execute(self,cpu):
        cpu.changeState()
        i = cpu.getPCB().getPC()
        while (i < cpu.getPCB().getSize()):
            instruction = cpu.getMMU().getInstruction(i,cpu.getPCB().getPid())
            if (not instruction.isIO()):
                i += 1
                cpu.getPCB().setPC(i)
                instruction.execute(cpu)
                time.sleep(2)
            else:
                instruction.execute(cpu)
                break
        # BORRAR MEMORIA
        cpu.changeState()
        kernel_semaphore.release()
        
        
    
        
        
class Busy():
    
    def changeState(self,cpu):
        print "CPU: Changing to idle state.. "
        cpu.state = Idle()
    
    def execute(self,program,cpu):
        cpu.scheduler.add(program)
    
    