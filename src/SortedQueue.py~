'''
Created on 29/09/2013

@author: matlock
'''


from Queue import Queue
import threading
import time

io_semaphore = threading.Semaphore(0)
kernel_semaphore2 = threading.Semaphore(0)

class IOQueue(threading.Thread):
    
    def __init__(self,scheduler):
        threading.Thread.__init__(self)
        self.queue = Queue()
        self.scheduler = scheduler
        
    def isEmpty(self):
        return self.queue.empty()
        
        
    def setScheduler(self,scheduler):
        self.scheduler = scheduler
        
    def put(self,pcb):
        self.queue.put(pcb)
        
    def pop(self):
        time.sleep(5)
        pcb = self.queue.get()
        pcb.setPC(pcb.getPC() + 1)
        print "I/O QUEUE:   Executing a I/O instruction.. "
        print "I/O QUEUE: "+"'"+pcb.getPid()+"'"+":  ends the I/O instruction "
        self.scheduler.add(pcb)
        kernel_semaphore2.release()
        
    def shutDown(self):
        print "I/O QUEUE: Shutdown!! "
        
    def run(self):
        while (True):
            io_semaphore.acquire()
            self.pop()
    



class SortedQueue():
    
    def __init__(self):
        self.myList = []
        self.condition_var =threading.Condition(threading.RLock())
        
        
    def get(self):
        try:
            self.condition_var.acquire()
            while(self.isEmpty(self.myList)):
                self.condition_var.wait()
            return self.myList.pop(0)
        finally:
            self.condition_var.release() 
            
    def __len__(self):
        return len(self.myList)   
    
    def isEmpty(self, aList):
        return len(aList) == 0  
    
    def sort(self):
        try:
            self.condition_var.acquire()
            for i in range(1,len(self.myList)):
                saver = self.myList[i]
                index = i
                while (index > 0 and self.myList[index - 1] > saver):
                    self.myList[index] = self.myList[index - 1]
                    index -= 1
                self.myList[index] = saver
        finally:
            self.condition_var.release()
            
    def put(self, anObject):
        try:
            self.condition_var.acquire()
            self.myList.append(anObject)
            self.sort()    
            self.condition_var.notifyAll()
        finally:
            self.condition_var.release()
            

# WITH RECURSION !
    def cons(self,anObject,aList):
        aList.insert(0,anObject)
        return aList
            
    def head(self,aList):
        return aList[0]
    
    def tail(self,aList):
        aList.pop()
        return aList
    
    
    # Another way of putting an Object    
    def insertion(self,anObject, aList):
        try:
            self.condition_var.acquire()    
            # Base case !!
            if (len(aList) == 0):
                aList.append(anObject) 
                return aList
            # Recursive case!! 
            else:
                if(anObject < aList[0]):
                    self.cons(anObject, aList)
                    return aList
                else:
                    x = self.head(aList)
                    return self.cons(x,(self.insertion(anObject,self.tail(aList))))
        finally:
            self.condition_var.notifyAll()
            self.condition_var.release()