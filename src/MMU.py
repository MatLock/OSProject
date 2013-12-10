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
    
    def __init__(self):
        self.emptyFrames = []
        self.fullFrames = []
        #AGREGAR ALGORITMO DE MANEJO DE MEMORIA!!
        
        
    def getMemory(self):
        if(not len(self.emptyFrames) == 0):
            return self.emptyFrames[0].getMemory()
        else:
            return self.fullFrames[0].getMemory()
        
    def load(self,pcb,program):
        try:
            conditionMMU.acquire()
            frame = self.selectEmptyFrame(pcb.getSize())
            if(frame.getSize() > pcb.getSize()):
                result = frame.splitFrame(pcb.getSize())
                result.load(pcb,program)
                self.fullFrames.append(result)
                self.addEmptyFrame(frame)
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
            size = frame.getSize()
            self.fullFrames.remove(frame)
            print ("MMU: The frame has been emptied")
            self.emptyFrames.append(frame)
            return size
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
    
    def buildEmptyFrame(self,aList):
        frame = Frame(self.fullFrames[0].getMemory(),aList[0],len(aList))
        return frame
            
            
    def compact(self):
        try:
            conditionMMU.acquire()
            if (len(self.emptyFrames) > 0):
                x = len(self.fullFrames)
                for i in range(0,x):
                    fullFrame = self.fullFrames[i]
                    fullFrame.moveUp()
                self.emptyFrames = []
                self.addEmptyFrame(self.buildEmptyFrame(self.fullFrames[0].getMemory().getEmptyCells()))
        finally:
            conditionMMU.release()
        
            
    def getInstruction(self,index,pid):
        try:
            conditionMMU.acquire()
            return self.getFrame(pid).getInstruction(index)
        finally: 
            conditionMMU.release()
            
    def selectEmptyFrame(self,size):
        try:
            conditionMMU.acquire()
            i = 0
            while (i < len(self.emptyFrames)):
                x = self.emptyFrames[i]
                if (x.getSize() >= size):
                    return self.emptyFrames.pop(i)
                raise Exception ("There isn't any frame to allocate the program!")
        finally:
            conditionMMU.release()
    
    def getBase(self,size):
        try:
            conditionMMU.acquire()
            i = 0
            while(len(self.emptyFrames) > i):
                if(self.emptyFrames[i].getSize() >= i):
                    return self.emptyFrames[i].getBase()
                i += 1
            raise Exception ("There isn't any frame to allocate the program!")
        finally:
            conditionMMU.release()
    
    def addEmptyFrame(self,frame):
        self.emptyFrames.append(frame) 
        
    def printMemory(self):
        self.fullFrames[0].memory.printMemory()