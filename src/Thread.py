'''
Created on 23/09/2013

@author: matlock
'''

import threading
import time

semaphore = threading.Semaphore(0)

class Thread(threading.Thread):
    
    def __init__(self, num, pid, size):
        threading.Thread.__init__(self)
        self.priority = num
        self.id = pid
        self.size = size
        
    def getPriority(self):
        return self.priority
        
    def execute(self,i):
        print "I'm the thread : " + str(self.id)+ "  executing instruction number: " + str(i) + "  of  " + str(self.size)
        time.sleep(2)
             
    def run(self):
        i = 1
        while (i <= self.size):
            self.execute(i)
            i+= 1
        semaphore.release()
