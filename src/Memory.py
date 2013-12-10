'''
Created on 08/10/2013

@author: matlock,santiago
'''

class Memory():
    
    def __init__(self,):
        self.blocks = {}
        self.size = 0

    def buildMemory(self,size):
        for i in range(0,size):
            self.blocks[i] = None
        self.size = size
            
    def getSize(self):
        return self.size

    def load (self,number,instruction):
        self.blocks[number] = instruction
    
    def getInstruction(self,index):
        return self.blocks.get(index)
    
    def isEmpty(self):
        return len(self.blocks)==0
        
    def printMemory(self):
        for i in range(0,20):
            print (self.blocks[i])
            
    def moveOnePlace(self,base,size):
        self.blocks[base - 1] = self.blocks[base]
        for i in range(0,size):
            self.blocks[base + i] = self.blocks[base + i + 1]
        self.blocks[base + size - 1] = None 
            
    def getEmptyCells(self):
        result = []
        for i in range(0,self.size):
            if(self.blocks[i] == None):
                result.append(i)
        return result
            
            
                            
                    
        
    
    
        
    