'''
Created on 23/09/2013

@author: matlock
'''

class Program():

    def __init__(self, num, identifier, boolean):
        self.priority = num
        self.id = identifier
        self.pc = 0
        self.size = 0
        self.isAPriority = boolean
        self.instructions = []

    def getIdentifier(self):
        return self.id
    
    def getPriority(self):
        return self.priority
        
    def __lt__(self,anotherObject):
        return self.getPriority() < anotherObject.getPriority()
    
    def __gt__(self,anotherObject):
        return self.getPriority() > anotherObject.getPriority()
    
    def addInstruction(self, anInstruction):
        self.instructions.append(anInstruction)
        self.size = self.size + 1

    def getInstruction(self,index):
        return self.instructions[index]
    
    def setIndex(self,index):
        self.pc = index
        
    def getIndex(self):
        return self.pc