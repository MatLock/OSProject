'''
Created on 23/09/2013

@author: matlock
'''

class Program():

    def __init__(self, num, identifier, size, boolean, pc):
        self.priority = num
        self.id = identifier
        self.pc = 0
        self.size = size
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

    def getInstruction(self,index):
        return self.instruction[index]
    
    def nextInstruction(self):
        return self.instructions[self.pc + 1]