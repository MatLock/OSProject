'''
Created on 19/11/2013

@author: Santi
'''
import unittest
from src.Program import *
from mockito import *


class TestProgram(unittest.TestCase):


    def setUp(self):
        self.program = Program("myProgram")
        self.instrucion = mock()




    def testAddInstruction(self):
        self.program.addInstruction(self.instrucion)
        self.assertEquals(self.program.getInstruction()[0],self.instrucion)
        self.assertEqual(len(self.program.instruction), 1)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()