'''
Created on 08/10/2013

@author: matlock
'''

class Memory():
    
    def __init__(self):
        self.blocks = {}
        

    def buildMemory(self,size):
        for i in range(0,size):
            self.blocks[i] = i

    def load (self,number,instruction):
        self.blocks[number] = instruction
    
    def getInstruction(self,index):
        return self.blocks.get(index)
    
    def isEmpty(self):
        return len(self.blocks)==0
    
    def size(self):
        return len(self.blocks)
    
    def printMemory(self):
        for i in range(0,9):
            print (self.blocks[i])
            
                            
                    
        
    
    
        
    