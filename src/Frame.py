'''
Created on 28/10/2013

@author: matlock
'''


class Frame():
    
    def __init__(self,memory,memoryBase):
        self.pcb = None
        self.memory = memory
        self.isEmpty = True
        self.base = memoryBase
        
    def getBase(self):
        return self.base
        
    def load(self,pcb,program):
        self.pcb = pcb
        for i in range(0,pcb.getSize()):
            self.memory.load(self.base + i,program.instruction[i])
            i+= 1
        self.isEmpty = False
        
    def getInstruction(self,index):
        return self.memory.blocks.get(self.base + index)
    
    def getPCB(self):
        return self.pcb
    
    def isEmpty(self):
        return self.isEmpty
        
    