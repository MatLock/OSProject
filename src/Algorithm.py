'''
Created on 23/09/2013

@author: matlock
'''


from Queue import Queue
from SortedQueue import *


class FIFO():

    def __init__(self):
        self.queue = Queue()

    def add(self, pcb):
        self.queue.put(pcb)

    def get(self):
        return self.queue.get()
    
    def isEmpty(self):
        return self.queue.empty()
            
class PFIFO():
    
    def __init__(self):
        self.queue = Queue()
        self.priorityQueue = SortedQueue()
    
    def add(self, element):
        if (element.isAPriority):
            self.priorityQueue.put(element)
        else:
            self.queue.put(element)
    
    def get(self):
        if (len (self.priorityQueue) == 0):
            return self.queue.get()
        return self.priorityQueue.get()
    
    def isEmpty(self):
        return self.priorityQueue == 0 and self.queue == 0
    

