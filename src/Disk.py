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
        
    def isEmpty(self):
        return len(self.programList) == 0
    
    def save(self,program):
        self.programList.append(program)
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def get(self,size):
        for i in range(len(self.programList)):
            if (len(self.programList[i]) == size):
                self.getKernel().saveProgram(self.programList[i])
                return 0