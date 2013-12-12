'''
Created on 18/11/2013

@author: matlock
'''

from src.Memory import *
from src.Frame import *
from src.MMU import *
from src.Instruction import *
from src.Program import *
from src.PCB import *
from src.Logger import *


import unittest 

class testMMU(unittest.TestCase):
    
    def setUp(self):
        self.instruction1 = BasicInstruction()     
        self.memory = Memory()
        self.memory.buildMemory(5)
        self.frame1 = Frame(self.memory,0,1)
        self.frame2 = Frame(self.memory,1,2)
        self.frame3 = Frame(self.memory,3,1)
        self.frame4 = Frame(self.memory,4,1)
        self.logger = Logger("/home/matlock/Escritorio/Sistemas Operativos/OSProyect/resource/log.txt")
        self.mmu = MMU(self.logger)
        self.mmu.fullFrames.append(self.frame1)
        self.mmu.fullFrames.append(self.frame3)
        self.mmu.emptyFrames.append(self.frame2)
        self.mmu.emptyFrames.append(self.frame4)
        self.program = Program('a')
        self.program.addInstruction(self.instruction1)
        self.pcbA = PCB('a',0,0,1)
        self.programb = Program('b')
        self.pcbB = PCB('b',0,3,1)
        self.programb.addInstruction(self.instruction1)
        self.frame1.load(self.pcbA,self.program)
        self.frame3.load(self.pcbB,self.programb)
        self.programc = Program('c')
        self.programc.addInstruction(self.instruction1)
        self.programc.addInstruction(self.instruction1)
        self.programc.addInstruction(self.instruction1)
        self.pcbC = PCB('c',0,3,3)
        
    def testCompact(self):
        self.memory.printMemory()
        self.mmu.compact()
        base = self.mmu.emptyFrames[0].getBase()
        self.mmu.load(self.pcbC,self.programc,base)
        for i in range(0,5):
            instruction = self.memory.blocks[i]
            self.assertIsInstance(instruction, BasicInstruction, "Compact test")
        print( "                                   ")
        self.memory.printMemory()
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        