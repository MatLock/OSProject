'''
Created on 07/10/2013

@author: matlock
'''

import threading
from src.Program import *

conditionMMU = threading.Condition(threading.RLock())

class MMU():
    
    def __init__(self):
        self.emptyFrames = []
        self.fullFrames = []
        #AGREGAR ALGORITMO DE MANEJO DE MEMORIA!!
        
        
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
            self.fullFrames.remove(frame)
            print ("MMU: The frame has been emptied")
            self.emptyFrames.append(frame)
        finally:
            conditionMMU.release()
            
            
    def compact(self):
        try:
            conditionMMU.acquire()
            pcbs = []
            current = []
            x = len(self.fullFrames)
            for i in range(0,x):
                y = self.fullFrames[i]
                pcbs.append(y.getPCB())
                program = Program(y.getPCB().getPid())
                program.setList(y.getAll())    
                current.append(program)
            frame = self.emptyFrames.pop(0)
            frame.reset()
            self.emptyFrames = []
            self.fullFrames = []
            self.addEmptyFrame(frame)
            for i in range(0,x):
                self.load(pcbs[i],current[i])
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
                x = self.emptyFrames.pop(i)
                if (x.getSize() >= size):
                    self.emptyFrames.insert(i,x)
                    return x
                raise Exception ("There isn't any space to allocate the program!")
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
            raise Exception ("There isn't any space to allocate the program!")
        finally:
            conditionMMU.release()
    
    def addEmptyFrame(self,frame):
        self.emptyFrames.append(frame) 
        
    def printMemory(self):
        self.fullFrames[0].memory.printMemory()