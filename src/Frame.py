'''
Created on 28/10/2013

@author: matlock
'''


class Frame():
    
    def __init__(self,memory,memoryBase,size):
        self.pcb = None
        self.memory = memory
        self.isEmpty = True
        self.base = memoryBase
        self.size = size
        
    def setBase(self,number):
        self.base = number
        
    def getSize(self):
        return self.size
    
    def getBase(self):
        return self.base
    
    def setSize(self,size):
        self.size = size
        
    def getMemory(self):
        return self.memory
    
      
    def getPCB(self):
        return self.pcb
    
    def isEmpty(self):
        return self.isEmpty
    
    def load(self,pcb,program):
        self.pcb = pcb
        for i in range(0,pcb.getSize()):
            self.memory.load(self.base + i,program.instruction[i])
            i+= 1
        self.isEmpty = False
    
    def moveUp(self):
        x = self.base
        while((self.getBase() > 0) and (self.memory.blocks[self.base - 1] == None)):
            self.setBase(self.getBase() - 1)
            self.getPCB().setBase(self.getBase() - 1)
            self.memory.moveOnePlace(x,self.size)
            x -= 1   
        
    def splitFrame(self,size):
        frame = Frame(self.memory,self.base,size)
        self.setBase(self.getBase() + size)
        self.setSize(self.getSize() - size)
        return frame
        
    def delete(self):
        for i in range(0,self.getSize()):
            self.memory.blocks[self.getBase() + i] = None
        
    def getInstruction(self,index):
        return self.memory.blocks.get(self.base + index)
   
        
    