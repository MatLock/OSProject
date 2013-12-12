'''
Created on 22/11/2013

@author: matlock
'''
import unittest
from mockito import *
from src.CPU import *



class TestCPU(unittest.TestCase):


    def setUp(self):
        self.state = mock()
        self.kernel = mock()
        self.mmu = mock()
        self.pcb = mock()
        self.timer = mock()
        self.logger = mock()
        self.cpu=CPU(self.kernel,self.mmu,self.pcb,self.timer,self.logger)
        self.cpu.setState(self.state)
    
        
        
    
    def testChangeState(self):
        self.cpu.changeState()
        verify(self.state).changeState(self.cpu)
        
    def testExecute(self):
        self.cpu.execute()
        verify(self.state).execute
        
        
    def testExecuteIOinstruction(self):
        self.cpu.executeIOinstruction()
        verify(self.kernel).sendToIO(self.pcb)
        
  
        
    def testContextSwitching(self):
        self.cpu.contextSwitching()
        verify(self.timer).reset()
        verify(self.state).changeState(self.cpu)
        
        
           
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()