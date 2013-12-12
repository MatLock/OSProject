'''
Created on 09/12/2013

@author: matlock,santiago
'''

from src.Kernel import *
from src.Logger import *


class Factory:
    
    def __init__(self,logger):
        self.logger = logger
        
    
    
    def create(self):
        x = []
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
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        program.addInstruction(instruction1)
        programd = Program('d')
        programd.addInstruction(instruction1)
        programd.addInstruction(instruction1)
        programd.addInstruction(instruction1)
        programb = Program('b')
        programb.addInstruction(instruction3)
        programb.addInstruction(instruction3)
        programb.addInstruction(instruction3)
        programb.addInstruction(instruction3)
        programc = Program('c')
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programc.addInstruction(instruction1)
        programe = Program('e')
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        programe.addInstruction(instruction1)
        timer = Timer(2)
        memory = Memory()
        memory.buildMemory(20)
        frame1 = Frame(memory,0,20)
        logger = Logger("/home/matlock/Escritorio/Sistemas Operativos/OSProyect/resource/log.txt")
        mmu = MMU(logger)
        mmu.addEmptyFrame(frame1)
        cpu = CPU(None,mmu,None,timer,logger)
        scheduler = Scheduler(PFIFO())
        ioqueue = IOQueue(scheduler,logger)
        disk = Disk(None)
        kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk,logger)
        disk.setKernel(kernel)
        cpu.setKernel(kernel)
        x.append(program)
        x.append(programb)
        x.append(programc)
        x.append(programd)
        x.append(programe)
        kernel.saveOnDisk(x)
        y = ['a','b','c','d','e']
        h = (y,kernel)
        return h
        