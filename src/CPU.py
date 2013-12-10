'''
Created on 30/09/2013

@author: matlock,santiago
'''
import threading
import time 

  
cpu_semaphore = threading.Semaphore(0)   
kernel_semaphore = threading.Semaphore(1)    
    
class CPU(threading.Thread):
    
    def __init__(self,kernel,mmu,pcb,timer,logger):
        threading.Thread.__init__(self)
        self.state = Idle()
        self.kernel = kernel
        self.timer = timer
        self.mmu = mmu
        self.pcb = pcb
        self.logger = logger
        
    def getLogger(self):
        return self.logger
        
    def setState(self,state):
        self.state=state
    
    def setKernel(self,kernel):
        self.kernel = kernel
    
    def setPCB(self,pcb):
        self.pcb = pcb
        
    def printState(self):
        return self.state.printState()
    
    
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
        self.getLogger().write("CPU: Context Switching.. \n")
        self.changeState()
        self.getLogger().write("CPU: Cpu is now" +"'"+str(self.state.printState())+"' \n")
        self.getTimer().reset()
        kernel_semaphore.release()
        
    def executePriorityInstruction(self):
        self.getLogger().write("CPU: Running a Priority Instruction of the program:   " + str(self.getPCB().getPid())+"\n")
            
    def executeBasicInstruction(self):
        self.getLogger().write("CPU: Running a basic instruction of the program:   " + str(self.getPCB().getPid())+"\n")
        
    def shutDown(self):
        self.getLogger().write("CPU: Shutdown!!  \n")
    
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
                time.sleep(2)
            else:
                instruction.execute(cpu)
                break
        if (pc == cpu.getPCB().getSize()):
            cpu.getKernel().delete(identifier)
            cpu.getLogger().write("CPU: Program " + str(identifier)+ " completed! \n")
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
    
    