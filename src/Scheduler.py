'''
Created on 07/10/2013

@author: matlock
'''

class Scheduler():
    
    def __init__(self,algorithm):
        self.algorithm = algorithm
        
    def add(self,pcb):
        self.algorithm.add(pcb)
        
    def get(self):
        return self.algorithm.get()
    
    def isEmpty(self):
        return self.algorithm.isEmpty()