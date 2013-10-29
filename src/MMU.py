'''
Created on 07/10/2013

@author: matlock
'''


class MMU():
    
    def __init__(self):
        self.emptyFrames = []
        self.fullFrames = []
        #AGREGAR ALGORITMO DE MANEJO DE MEMORIA!!
        
        
    def load(self,pcb,program):
        frame = self.selectEmptyFrame()
        frame.load(pcb,program)
        self.fullFrames.append(frame)
        
    def sizeFullFrame(self):
        return len(self.fullFrames)
    
    def sizeEmptyFrame(self):
        return len(self.emptyFrames)
        
    def getFrame(self,pid):
        for i in range(0,self.sizeFullFrame()):
            if (self.fullFrames[i].getPCB().getPid() == pid):
                return self.fullFrames[i]  
            else:
                i += 1
        raise "Frame doesn't found"
            
    def getInstruction(self,index,pid):
        return self.getFrame(pid).getInstruction(index)
        
    def selectEmptyFrame(self):
        return self.emptyFrames.pop()
    
    def getBase(self):
        return self.emptyFrames[0].getBase()
    
    def addEmptyFrame(self,frame):
        self.emptyFrames.append(frame) 