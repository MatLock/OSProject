'''
Created on 19/11/2013

@author: Santi
'''
import unittest
from src.Program import *
from unittest.mock import Mock


class TestProgram(unittest.TestCase):


    def setUp(self):
        self.program = Program("myProgram")
        self.instrucion=Mock()




    def testAddInstruction(self):
        self.program.addInstruction(self.instrucion)
        self.assertEquals(self.program.getInstruction()[0],self.instrucion)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()