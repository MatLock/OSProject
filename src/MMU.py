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
        try:
            for i in range(0,self.sizeFullFrame()):
                if (self.fullFrames[i].getPCB().getPid() == pid):
                    return self.fullFrames[i]  
                i += 1
        except:
            "Frame doesn't found"
    
    def delete(self,pid):
        frame = self.getFrame(pid)
        frame.delete()
        self.fullFrames.remove(frame)
        print ("MMU: The frame has been emptied")
        self.emptyFrames.append(frame)
            
    def getInstruction(self,index,pid):
        return self.getFrame(pid).getInstruction(index)
        
    def selectEmptyFrame(self):
        return self.emptyFrames.pop(0)
    
    def getBase(self):
        return self.emptyFrames[0].getBase()
    
    def addEmptyFrame(self,frame):
        self.emptyFrames.append(frame) 