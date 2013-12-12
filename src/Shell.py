'''
Created on 06/12/2013

@author: matlock,satiago
'''

from src.Kernel import *
from service.UserDAO import *
from src.Factory import *



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
        self.logger = Logger("/home/matlock/Escritorio/Sistemas Operativos/OSProyect/resource/log.txt")
        self.factory = Factory(self.logger)

    def getActualUser(self):
        print(self.actualUser)
        
    def setKernel(self,kernel):
        self.kernel = kernel
        
    def setProgramsID(self,programs):
        self.programsID = programs
        
    def printProgramsID(self):
        print (self.programsID)
        
    def addUser(self):
        newUser = raw_input("New user: ")
        password = raw_input("Enter the new password: ")
        anId = raw_input("Enter an unique ID: ")
        UserDAO().addUser(newUser,password,anId)
        
    def changePassword(self):
            oldPassword = raw_input("Enter the old password: ")
            result = UserDAO().getField("PASSWORD",self.actualUser)
            if (result[0][0] == oldPassword):
                print("Correct Password!")
                newPassword = raw_input("Enter the new password please:")
                result.refreshField("PASSWORD",self.actualUser,newPassword)
            else:
                raise Exception("User doesn't exist!")
        
    def validate(self,user,password):
        result = UserDAO().get(user, password)
        try:
            if (result[0][0] == user and result[0][1] == password):
                print("Welcome:  " + str(user))
        except (Exception):
            raise Exception ("Wrong password or id!")
    
    
    def help(self):
        print("Commands are: \n" +str(self.methods.keys()))
        
    def initialize(self):
        self.logger.readPresentation()
        
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
        self.logger.read()
        
    def build(self):
        x = self.factory.create()
        self.setProgramsID(x[0])
        self.setKernel(x[1])
        
    def run(self):
        self.initialize()
        pompt = " -> "
        print (pompt + "Please Log in: ")
        self.loggIn()
        self.build()
        print ("Programs on disk are:")
        print(self.programsID)
        while (True):
            print(pompt + "What do you wanna do?")
            inputUser = (raw_input(pompt + str(self.actualUser+": ")))
            if(not inputUser == ''):
                value = inputUser.split() 
                if (value[0] == "execute"):
                    idProgram = raw_input(pompt + "Please enter an ID:")
                    self.execute(idProgram)
                elif (not self.methods.has_key(value[0])):
                    raise Exception("I don't understand!!")
                else:
                    method = self.methods[value[0]]
                    method()
                            
                
def main():
    s = Shell()
    s.run()
    
if __name__ == '__main__':
    main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            