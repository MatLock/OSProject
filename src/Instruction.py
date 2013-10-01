

class BasicInstruction():
    
    def __init__(self, name):
        self.name = name
        
    def execute(self):
        print self.name
            

class IO_Instruction(BasicInstruction):
    
    def __init__(self,name):
        self.name = name
        
    def execute(self):
        print self.name
    
    
    
    
        