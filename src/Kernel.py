'''
Created on 30/09/2013

@author: matlock
'''
import Queue
import threading
from SortedQueue import *

io_semaphore = threading.Semaphore(0)
kernel_semaphore = threading.Semaphore(1)
cpu_semaphore = threading.Semaphore(0)

class Kernel(threading.Thread):
    
    def __init__(self,scheduler,cpu):
        threading.Thread.__init__(self)
        self.scheduler = scheduler
        self.cpu = cpu
        self.ioQueue = IOQueue()
        
    def execute(self,program):
        if (self.scheduler.isEmpty()):
            self.cpu.execute(program)
        else:
            self.scheduler.add(program)
        
    def run(self):
        while(True):
            kernel_semaphore.acquire()
            
            
        
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
    
    def __init__(self,kernel,scheduler):
        threading.Thread.__init__(self)
        self.kernel = kernel
        self.scheduler = scheduler
        self.state = Idle()
        self.pcb = None
         
        " PCB = PC OF PROGRAM"
                "ID OF PROGRAM"
    def changeState(self):
        self.state.changeState(self)
    
    def execute(self,pcb):
        self.state.execute(self)
        
    def run(self):
        while(True):
            cpu_semaphore.acquire()
            
            
            
        
class Idle():
    
    def changeState(self,cpu):
        cpu.state = Busy()
        
    def execute(self, cpu):
        cpu.changeState()
        " tocar aca"
        kernel_semaphore.release()
        io_semaphore.release()
        
        
class Busy():
    
    def changeState(self,cpu):
        cpu.state = Idle()
    
    def execute(self,program,cpu):
        cpu.scheduler.add(program)
        

    
        
    