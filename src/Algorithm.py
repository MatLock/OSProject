'''
Created on 23/09/2013

@author: matlock
'''

from Thread import *
from Queue import Queue


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


def main():
    x = Thread(1, 'a', 3)
    y = Thread(2, 'b', 4)
    algorithm = FIFO()
    algorithm.add(x)
    algorithm.add(y)
    algorithm.start()

if __name__ == '__main__':

    main()



