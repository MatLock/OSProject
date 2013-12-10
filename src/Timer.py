'''
Created on 04/11/2013

@author: matlock,santiago
'''

class Timer():
    
    def __init__(self,aNumber):
        self.quantum = aNumber
        self.actual_value = 0
        
    def getActualValue(self):
        return self.actual_value
    
    def increaseActualValue(self):
        self.actual_value += 1
        
    def reset(self):
        self.actual_value = 0
        
    def isEnded(self):
        return self.quantum == self.actual_value 
        