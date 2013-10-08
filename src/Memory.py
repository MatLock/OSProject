'''
Created on 08/10/2013

@author: matlock
'''

class Memory():
    
    def __init__(self):
        self.blocks = {}
        
        
    def load (self,pid,base,program):
        self.blocks[pid]=program
        
    def getInstruction(self,index,pid):
        return self.blocks.get(pid).instruction[index]
    
    
        
    