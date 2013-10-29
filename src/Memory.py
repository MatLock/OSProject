'''
Created on 08/10/2013

@author: matlock
'''

class Memory():
    
    def __init__(self):
        self.blocks = {}
        

    def buildMemory(self,size):
        for i in range(0,size):
            self.blocks[i] = None

    def load (self,number,instruction):
        self.blocks[number] = instruction
        
    def getInstruction(self,index):
        return self.blocks.get(index)
    
    def isEmpty(self):
        return len(self.blocks)==0
    
    def size(self):
        return len(self.blocks)
    
    
    def checkForRoom(self,programSize,aPlace):
        i=1
        while(i<programSize):
            if(self.blocks[aPlace+1]==None):
                i+=1
            else:
                return False
        return True
            
    def getFirstFreeCell(self):
            i=1
            while(i <= self.size()):
                if(not self.blocks[i]==None):
                    i+=1
                return i
          
    
    def getBase(self,programSize):
        if(self.isEmpty()):
            return 0
        elif(self.checkForRoom(programSize,self.getFirstFreeCell())):
            return self.getFirstFreeCell()
        else:
            return None
            
                            
                    
        
    
    
        
    