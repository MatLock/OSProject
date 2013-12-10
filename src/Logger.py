'''
Created on 09/12/2013

@author: matlock,santiago
'''
import os  

class Logger:
    
    def __init__(self,path):
        self.path = path
        
    def write(self,message):
        log = open(self.path,"a")
        log.write(message)
        log.close()
        
        
    def read(self):
        log = open(self.path,"r")
        print(log.read())
        log.close()
        
    def readPresentation(self):
        log = open("/home/matlock/Escritorio/Sistemas Operativos/OSProyect/resource/presentation.txt","r")
        print(log.read())
        log.close()
        
        
def main():
    l = Logger("/home/matlock/Escritorio/Sistemas\ Operativos/OSProyect/resource/log.txt")
    l.write("hola")
    print(l.read())
  
    
    
if __name__ == '__main__':
    main()