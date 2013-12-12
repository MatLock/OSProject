'''
Created on 07/10/2013

@author: matlock,santiago
'''

from src.Program import * 
from  src.Disk import *
from src.Frame  import *
import threading 

conditionMMU = threading.Condition(threading.RLock())

class MMU():
    
    def __init__(self,logger):
        self.emptyFrames = []
        self.fullFrames = []
        self.logger = logger
        
        
    def getMemory(self):
        if(not len(self.emptyFrames) == 0):
            return self.emptyFrames[0].getMemory()
        else:
            return self.fullFrames[0].getMemory()
        
    def getLogger(self):
        return self.logger
        
    def load(self,pcb,program,base):
        try:
            conditionMMU.acquire()
            frame = self.selectEmptyFrame(base)
            if(frame.getSize() > pcb.getSize()):
                result = frame.splitFrame(pcb.getSize())
                result.load(pcb,program)
                self.fullFrames.append(result)
                self.emptyFrames.append(frame)
            else:
                frame.load(pcb,program)
                self.fullFrames.append(frame) 
        finally:
            conditionMMU.release()
        
    def sizeFullFrame(self):
        return len(self.fullFrames)
    
    def sizeEmptyFrame(self):
        return len(self.emptyFrames)
        
    def getFrame(self,pid):
        try:
            conditionMMU.acquire()
            for i in range(0,self.sizeFullFrame()):
                if (self.fullFrames[i].getPCB().getPid() == pid):
                    return self.fullFrames[i]  
                i += 1
        finally:
            conditionMMU.release()
    
    def delete(self,pid):
        try:
            conditionMMU.acquire()
            frame = self.getFrame(pid)
            frame.delete()
            self.fullFrames.remove(frame)
            self.getLogger().write("MMU: The frame has been emptied \n")
            self.emptyFrames.append(frame)
        finally:
            conditionMMU.release()
            
    def selectMinor(self):
        frame = self.emptyFrames[0]
        result = 0
        for i in range(1,len(self.emptyFrames)):
            if (frame.getBase() < self.emptyFrames[i].getBase()):
                frame = self.emptyFrames[i]
                result = i
        return self.emptyFrames.pop(result)
    
    def buildEmptyFrame(self,memory,aList):
        frame = Frame(memory,aList[0],len(aList))
        return frame
            
            
    def compact(self):
        try:
            conditionMMU.acquire()
            x = len(self.fullFrames)
            for i in range(0,x):
                fullFrame = self.fullFrames[i]
                fullFrame.moveUp()
            memory = self.getMemory()
            self.emptyFrames = []
            self.addEmptyFrame(self.buildEmptyFrame(memory,memory.getEmptyCells()))
        finally:
            conditionMMU.release()
        
            
    def getInstruction(self,index,pid):
        try:
            conditionMMU.acquire()
            return self.getFrame(pid).getInstruction(index)
        finally: 
            conditionMMU.release()
    '''        
    def getIndexByBase(self,base):
        for i in range(0,(len(self.emptyFrames))):
            if (self.emptyFrames[i].getBase() == base):
                return i
   
    def selectEmptyFrame(self,base):
        try:
            conditionMMU.acquire()
            return self.emptyFrames.pop(self.getIndexByBase(base))
        finally:
            conditionMMU.release()
     '''       
    def selectEmptyFrame(self,base):
        try:
            conditionMMU.acquire()
            for i in range(0,len(self.emptyFrames)):
                if(base == self.emptyFrames[i].getBase()):
                    return self.emptyFrames.pop(i)
        finally:
            conditionMMU.release()     
             
    def getBase(self,size):
        try:
            conditionMMU.acquire()
            for i in range(0,(len(self.emptyFrames))):
                if(self.emptyFrames[i].getSize() >= size):
                    return self.emptyFrames[i].getBase()
                else:
                    raise Exception ("There isn't any frame to allocate the program!")
        finally:
            conditionMMU.release()
    
    def addEmptyFrame(self,frame):
        self.emptyFrames.append(frame) 
        
    def printMemory(self):
        self.fullFrames[0].memory.printMemory()