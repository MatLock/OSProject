class Instruction():
    
    def execute(self,cpu):
        pass
    
    def io(self):
        pass

class BasicInstruction(Instruction):
        
    def execute(self,cpu):
        cpu.executeBasicInstruction()
        
    def io(self):
        return False
            

class IO_Instruction(Instruction):
        
    def execute(self,cpu):
        cpu.executeIOinstruction()
        
    def io(self):
        return True
        
    
    
    
    
        