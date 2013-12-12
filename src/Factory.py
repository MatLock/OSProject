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
        programsList = []
        
        basicIns = BasicInstruction()
        ioIns = IO_Instruction()
        prioIns = Priority_Instruction()
        
        program = Program('a')
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(ioIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        program.addInstruction(basicIns)
        
        programd = Program('d')
        programd.addInstruction(basicIns)
        programd.addInstruction(basicIns)
        programd.addInstruction(basicIns)
        
        programb = Program('b')
        programb.addInstruction(prioIns)
        programb.addInstruction(prioIns)
        programb.addInstruction(prioIns)
        programb.addInstruction(prioIns)
        
        programc = Program('c')
        programc.addInstruction(basicIns)
        programc.addInstruction(basicIns)
        programc.addInstruction(basicIns)
        programc.addInstruction(basicIns)
        programc.addInstruction(basicIns)
        programc.addInstruction(basicIns)
        
        programe = Program('e')
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        programe.addInstruction(basicIns)
        
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
        
        programsList.append(programd)
        programsList.append(programc)
        programsList.append(programe)
        programsList.append(programb)
        programsList.append(program)
        
        kernel.saveOnDisk(programsList)
        
        programsId = ['a','b','c','d','e']
        
        h = (programsId,kernel)
        
        return h
        