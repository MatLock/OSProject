'''
Created on 09/12/2013

@author: matlock,santiago
'''

from src.Kernel import *
from src.Logger import *
import os


class Factory:
    
    def __init__(self,logger):
        self.logger = logger
        
    
    
    def create(self):
        x = []
        y = []
        instruction1 = BasicInstruction()
        instruction2 = IO_Instruction()
        instruction3 = Priority_Instruction()
        program = Program('a')
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction2)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction2)
        program.addInstruction(instruction1)
        programb = Program('b')
        programb.addInstruction(instruction3)
        programc = Program('c')
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programd = Program('d')
        programd.addInstruction(instruction1)
        programd.addInstruction(instruction1)
        programe = Program('e')
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        x.append('a')
        x.append('b')
        x.append('c')
        x.append('d')
        x.append('e')
        y.append(program)
        y.append(programb)
        y.append(programc)
        y.append(programd)
        y.append(programe)
        timer = Timer(2)
        memory = Memory()
        memory.buildMemory(20)
        frame1 = Frame(memory,0,20)
        mmu = MMU()
        mmu.addEmptyFrame(frame1)
        cpu = CPU(None,mmu,None,timer,self.logger)
        scheduler = Scheduler(PFIFO())
        ioqueue = IOQueue(scheduler,self.logger)
        disk = Disk(None)
        kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk,self.logger)
        kernel.saveOnDisk(y)
        disk.setKernel(kernel)
        cpu.setKernel(kernel)
        h = (x,kernel)
        return h