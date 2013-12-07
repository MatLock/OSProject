'''
Created on 07/10/2013

@author: matlock
'''

class PCB():
    
    def __init__(self,pid,priority,base,size):
        self.pid = pid
        self.priority = priority
        self.pc = 0
        self.base = base
        self.size = size
        
    def getPid(self):
        return self.pid
    
    def getPC(self):
        return self.pc
    
    def getPriority(self):
        return self.priority
    
    def getBase(self):
        return self.base
    
    def getSize(self):
        return self.size
    
    def setPC(self,index):
        self.pc = index
        
    def setBase(self,aNumber):
        self.base = aNumber
        
    def __lt__(self,pcb):
        return self.getPriority() < pcb.getPriority()
    
    def __gt__(self,pcb):
        return self.getPriority() > pcb.getPriority()