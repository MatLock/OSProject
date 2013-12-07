'''
Created on 23/09/2013

@author: matlock
'''


from SortedQueue import SortedQueue
from Queue import Queue


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
    
    def add(self, pcb):
        if (pcb.getPriority() == 1):
            self.priorityQueue.put(pcb)
        else:
            self.queue.put(pcb)
    
    def get(self):
        if (len (self.priorityQueue) == 0):
            return self.queue.get()
        return self.priorityQueue.get()
    
    def isEmpty(self):
        return self.priorityQueue.isEmpty() and self.queue.empty()
    
    

