'''
Created on 30/09/2013

@author: matlock
'''
import threading
import time 

  
cpu_semaphore = threading.Semaphore(0)   
kernel_semaphore = threading.Semaphore(1)    
    
class CPU(threading.Thread):
    
    def __init__(self,kernel,mmu,pcb,timer):
        threading.Thread.__init__(self)
        self.state = Idle()
        self.kernel = kernel
        self.timer = timer
        self.mmu = mmu
        self.pcb = pcb
        
    def setState(self,state):
        self.state=state
    
    def setKernel(self,kernel):
        self.kernel = kernel
    
    def setPCB(self,pcb):
        self.pcb = pcb
    
    
    def getMMU(self):
        return self.mmu
        
    def getPCB(self):
        return self.pcb
    
    def getKernel(self):
        return self.kernel
    
    def getTimer(self):
        return self.timer
    
    def changeState(self):
        self.state.changeState(self)
        
    def execute(self):
        self.state.execute(self)
 
    def executeIOinstruction(self):
        self.kernel.sendToIO(self.pcb)
        
    def contextSwitching(self):
        print ("CPU: Context Switching..")
        self.changeState()
        print ("CPU: Cpu is now " ) + "'"+str(self.state.printState())+"'"
        self.getTimer().reset()
        kernel_semaphore.release()
        
    def executePriorityInstruction(self):
        print ("CPU: Running a Priority Instruction of the program:   " + str(self.getPCB().getPid()))
        
    def executeBasicInstruction(self):
        print ("CPU: Running a basic instruction of the program:   " + str(self.getPCB().getPid()))
        
    def shutDown(self):
        print ("CPU: Shutdown!! ")
    
    def run(self):
        while(True):
            cpu_semaphore.acquire()
            self.execute()
        
class Idle(): 
    
    def changeState(self,cpu):
        cpu.state = Busy()
        
    def printState(self):
        return "Idle"
    
    def execute(self,cpu):
        cpu.changeState()
        pc = cpu.getPCB().getPC()
        identifier = cpu.getPCB().getPid()
        while (pc < cpu.getPCB().getSize() and not(cpu.getTimer().isEnded())):
            instruction = cpu.getMMU().getInstruction(pc,identifier)
            if (not instruction.isIO()):
                pc += 1
                cpu.getTimer().increaseActualValue()
                cpu.getPCB().setPC(pc)
                instruction.execute(cpu)
                time.sleep(0)
            else:
                instruction.execute(cpu)
                break
        if (pc == cpu.getPCB().getSize()):
            cpu.getKernel().delete(identifier)
            print ("CPU: Program " + str(identifier)+ " completed!")
        elif(not instruction.isIO()):
            cpu.getKernel().savePCB(cpu.pcb)
        cpu.contextSwitching()
        
        
class Busy():
    
    def changeState(self,cpu):
        cpu.state = Idle()
        
    def printState(self):
        return "Busy"
    
    def execute(self,program,cpu):
        cpu.scheduler.add(program)
    
    