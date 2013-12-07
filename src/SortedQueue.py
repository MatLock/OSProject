'''
Created on 29/09/2013

@author: matlock
'''


from Queue import Queue
import threading
import time

io_semaphore = threading.Semaphore(0)
kernel_semaphore2 = threading.Semaphore(0)
c_variable = threading.Condition(threading.RLock())

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
        log = open("../resource/log.txt","a")
        log.write("I/O QUEUE: Executing an I/O Instruction  \n"
                  "I/O QUEUE: "+"'"+pcb.getPid()+"'"+":  ends the I/O instruction  \n") 
        print ("I/O QUEUE:   Executing an I/O Instruction.. ")
        print ("I/O QUEUE: "+"'"+pcb.getPid()+"'"+":  ends the I/O instruction ")
        log.close()
        self.scheduler.add(pcb)
        kernel_semaphore2.release()
        
    def shutDown(self):
        log = open("../resource/log.txt", "a")
        log.write("I/O QUEUE: Shutdown!!  \n")
        log.close()
        print ("I/O QUEUE: Shutdown!! ")
        
    def run(self):
        while (True):
            io_semaphore.acquire()
            self.pop()
    



class SortedQueue():
    
    def __init__(self):
        self.myList = []
        self.condition_var =threading.Condition(threading.RLock())
        
    def isEmpty(self):
        return len(self.myList) == 0
        
    def __len__(self):
        return len(self.myList)
    
    def get(self):
        try:
            self.condition_var.acquire()
            while(self.isEmpty()):
                self.condition_var.wait()
            return self.myList.pop(0)
        finally:
            self.condition_var.release() 
    
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
        c_variable.acquire()    
        # Base case !!
        if (len(aList) == 0):
            aList.append(anObject) 
            return aList
        # Recursive case!! 
        elif(anObject < aList[0]):
            cons(anObject, aList)
            return aList
        else:
            x = head(aList)
            return cons(x,(insertion(anObject,tail(aList))))
    finally:
        c_variable.notifyAll()
        c_variable.release()