'''
Created on 23/09/2013

@author: matlock
'''

import threading
import time

semaphore = threading.Semaphore(0)


class Thread(threading.Thread):

    def __init__(self, num, identifier, size, bool):
        threading.Thread.__init__(self)
        self.priority = num
        self.id = identifier
        self.size = size
        self.isAPriority = bool

    def getIdentifier(self):
        return self.id
    
    def getPriority(self):
        return self.priority

    def execute(self, i):
        print "I'm the thread: "+str(self.id)+" executing instruction number: "+str(i)+" of "+str(self.size)+" Am I a Priority Thread??.. "+str(self.isAPriority)
        time.sleep(2)
        
    def __lt__(self,anotherObject):
        return self.getPriority() < anotherObject.getPriority()
    
    def __gt__(self,anotherObject):
        return self.getPriority() > anotherObject.getPriority()

    def run(self):
        i = 1
        while (i <= self.size):
            self.execute(i)
            i += 1
        semaphore.release()
