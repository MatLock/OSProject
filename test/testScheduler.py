'''
Created on 19/11/2013

@author: Santi
'''
import unittest
from mockito import *
from src.Scheduler import *


class Test(unittest.TestCase):


    def setUp(self):
        self.myAlgorithm=mock()
        self.myPcb=mock()
        self.myScheduler= Scheduler(self.myAlgorithm)


    def testAddPcb(self):
        self.myScheduler.add(self.myPcb)
        verify(self.myAlgorithm).add(self.myPcb)
       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()