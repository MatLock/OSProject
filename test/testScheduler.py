'''
Created on 19/11/2013

@author: Santi
'''
import unittest
from mockito import *
from src.Scheduler import *


class Test(unittest.TestCase):


    def setUp(self):
        self.myAlgorithm = mock()
        self.myPcb = mock()
        when(self.myPcb).getIdentifier().thenReturn('a')
        self.myScheduler = Scheduler(self.myAlgorithm)


    def testAddPcb(self):
        self.myScheduler.add(self.myPcb)
        verify(self.myAlgorithm).add(self.myPcb)
        self.assertEqual(self.myPcb.getIdentifier(),'a')     
    
    def testIsEmpty(self):
        self.myScheduler.isEmpty()
        verify(self.myAlgorithm).isEmpty()  
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()