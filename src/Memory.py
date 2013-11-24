'''
Created on 08/10/2013

@author: matlock
'''

class Memory():
    
    def __init__(self,):
        self.blocks = {}
        self.size = 0

    def buildMemory(self,size):
        for i in range(0,size):
            self.blocks[i] = i
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
        for i in range(0,5):
            print (self.blocks[i])
            
                            
                    
        
    
    
        
    