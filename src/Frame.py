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
    
    def load(self,pcb,program):
        self.pcb = pcb
        for i in range(0,pcb.getSize()):
            self.memory.load(self.base + i,program.instruction[i])
            i+= 1
        self.isEmpty = False
        
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
    
    def getAll(self):
        result = []
        for i in range(0,self.getSize()):
            result.append(self.getInstruction(i))
        return result    
            
    def reset(self):
        self.pcb = None
        self.isEmpty = True
        self.setBase(0)
        self.setSize(self.getMemory().getSize())
        self.delete()   
    
    def getPCB(self):
        return self.pcb
    
    def isEmpty(self):
        return self.isEmpty
        
    