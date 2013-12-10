'''
Created on 07/10/2013

@author: matlock,santiago
'''

class Program():
    
    def __init__(self,name):
        self.instruction = []
        self.name = name
        
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
        
    def setList(self,aList):
        self.instruction = aList
        
    def getInstruction(self):
        return self.instruction
        
    
    def addInstruction(self,anInstruction):
        self.instruction.append(anInstruction)
        
    