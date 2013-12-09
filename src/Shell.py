'''
Created on 06/12/2013

@author: matlock
'''

from src.Kernel import *
from service.UserDAO import *



class Shell:
 
    def __init__(self):
        self.kernel = None
        self.programsID = []
        self.actualUser = None
        self.methods ={"addUser" : self.addUser,
                       "stateOfCpu" : self.stateOfCpu,
                       "changePassword" : self.changePassword,
                       "readLog" : self.readLog,
                       "--help"  : self.help,
                       "actualUser" : self.getActualUser,
                       "programsID" : self.printProgramsID,
                       "execute '@param<Identifier>'" : None,
                       }

    def getActualUser(self):
        print(self.actualUser)
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def printProgramsID(self):
        print (self.programsID)
        
    def addUser(self):
        newUser = raw_input("New user: ")
        password = raw_input("Enter the new password: ")
        anId = raw_input("Enter an unique ID: ")
        userDAO = UserDAO()
        userDAO.addUser(newUser,password,anId)
        
    def changePassword(self):
            oldPassword = raw_input("Enter the old password: ")
            userDAO = UserDAO()
            result = userDAO.getField("PASSWORD",self.actualUser)
            if (result[0][0] == oldPassword):
                print("Correct Password!")
                newPassword = raw_input("Enter the new password please:")
                userDAO.refreshField("PASSWORD",self.actualUser,newPassword)
            else:
                raise Exception("User doesn't exist!")
        
    def validate(self,user,password):
        #PREGUNTAR COMO PUEDO ACCEDER DE MANERA ESTATICA.. (SIN INSTANCIAR)"
        userDAO = UserDAO()
        result = userDAO.get(user, password)
        try:
            if (result[0][0] == user and result[0][1] == password):
                print("Welcome:  " + str(user))
        except (Exception):
            raise Exception ("Wrong password or id!")
    
    
    def help(self):
        print("Commands are: \n" +str(self.methods.kfeeys()))
        
    def initialize(self):
        presentation = open("resource/presentation.txt","r")
        print(presentation.read())
        presentation.close()
        
    def loggIn(self):
        name = raw_input("Enter user name: ")
        password = raw_input("Enter the password: ")
        self.validate(name,password)
        self.actualUser = name
        
    def execute(self,anID):
        self.kernel.executeProgram(anID)
        
    def stateOfCpu(self):
        print(self.kernel.stateOfCpu())
        
    def readLog(self):
        log = open('resource/log.txt','r')
        print(log.read())
        log.close()
        
    def run(self):
        self.initialize()
        pompt = " -> "
        print (pompt + "Please Log in: ")
        self.loggIn()
        self.programsID = self.build()
        print ("Programs on disk are:")
        print(self.programsID)
        while (True):
            print(pompt + "What do you wanna do?")
            inputUser = (raw_input(pompt + str(self.actualUser+": ")))
            value = inputUser.split() 
            if (value[0] == "execute"):
                idProgram = raw_input(pompt + "Please enter an ID:")
                self.execute(idProgram)
            elif (not self.methods.has_key(value[0])):
                raise Exception("I don't understand!!")
            else:
                method = self.methods[value[0]]
                method()
                
    def build(self):
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
        cpu = CPU(None,mmu,None,timer)
        scheduler = Scheduler(PFIFO())
        ioqueue = IOQueue(scheduler)
        disk = Disk(None)
        kernel = Kernel(cpu,ioqueue,scheduler,mmu,disk)
        kernel.saveOnDisk(y)
        self.setKernel(kernel)
        disk.setKernel(kernel)
        cpu.setKernel(kernel)
        return x             
                
def main():
    s = Shell()
    s.run()
    
if __name__ == '__main__':
    main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            