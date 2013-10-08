'''
Created on 07/10/2013

@author: matlock
'''


class MMU():
    
    def __init__(self,memory):
        self.memory = memory
        
    # POR AHORA LE PASO EL IDENTIFICADOR.. NO LA BASE
    def load(self,pid,base,program):
        self.memory.load(pid,base,program)
        
    def getInstruction(self,index,pid):
        return self.memory.getInstruction(index,pid)
    
    # ESTE METODO TODAVIA NO LO USO
    def getBase(self):
        return self.memory.getBase()