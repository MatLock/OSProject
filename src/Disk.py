'''
Created on 23/11/2013

@author: matlock
'''

class Disk():
    
    def __init__(self,kernel):
        self.programList = []
        self.kernel = kernel
        
    def getKernel(self):
        return self.kernel
        
    def setKernel(self,kernel):
        self.kernel = kernel
    
    
    def isEmpty(self):
        return len(self.programList) == 0
    
    def save(self,program):
        self.programList.append(program)
        
    
        
    def getProgram(self,anIdentifier):
        for i in range(0,len(self.programList)):
            if (self.programList[i].getName() == anIdentifier):
                return self.programList.pop(i)
        raise Exception ("Identifier does not exist!")
        
    def get(self,size):
        for i in range(0,len(self.programList)):
            if (len(self.programList[i].getInstruction()) <= size):
                self.getKernel().saveProgram(self.programList[i])
                return 0