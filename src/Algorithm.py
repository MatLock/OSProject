'''
Created on 23/09/2013

@author: matlock
'''

from Thread import *
from Queue import Queue
from SortedQueue import *


class FIFO(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = Queue()

    def add(self, thread):
        self.queue.put(thread)

    def get(self):
        return self.queue.get()

    def execute(self):
        self.get().start()
        semaphore.acquire()

    def run(self):
        while (True):
            self.execute()
            
class PFIFO(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
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
    
    def execute(self):
        self.get().start()
        semaphore.acquire()
        
    def run(self):
        while (True):
            self.execute()

def main():
    x = Thread(0, 'x', 3,False)
    y = Thread(0, 'y', 4,False)
    h = Thread(0, 'h', 3,False)
    j = Thread(2, 'j', 1,True)
    p = Thread(1, 'p', 1,True)
    pfifo = PFIFO()
    pfifo.add(x)
    pfifo.add(y)
    pfifo.add(h)
    pfifo.add(j)
    pfifo.add(p)
    pfifo.start()

if __name__ == '__main__':

    main()



