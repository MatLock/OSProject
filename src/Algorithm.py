'''
Created on 23/09/2013

@author: matlock
'''


from Queue import Queue
from SortedQueue import *


class FIFO():

    def __init__(self):
        self.queue = Queue()

    def add(self, thread):
        self.queue.put(thread)

    def get(self):
        return self.queue.get()
    
    def isEmpty(self):
        return len(self.queue) == 0
            
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
    

