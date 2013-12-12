'''
Created on 09/12/2013

@author: matlock,santiago
'''

from service.DBConnector import *

class UserDAO:
    
    def get(self,user,password):
        try:
            connection = DBConnector().openConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT USER_ID,PASSWORD FROM  USER WHERE USER_ID = %s AND PASSWORD = %s;"
                           ,(user,password))
            return cursor.fetchall()
        finally:
            connection.close()
        
    def addUser(self,user,password,anID):
        try:
            connection = DBConnector().openConnection()
            cursor = connection.cursor()
            query = "INSERT INTO USER (USER_ID,PASSWORD,ID) VALUES (%s,%s,%s);"
            cursor.execute(query,(user,password,anID))
            connection.commit()
        finally:
            connection.close()
            
    def getField(self,field,user):
        try:
            connection = DBConnector().openConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT " +field+" FROM USER WHERE USER_ID = %s;",(user))
            return cursor.fetchall()
        finally:
            connection.close()
            
    def refreshField(self,field,user,newValue):
        try:
            connection = DBConnector().openConnection()
            cursor = connection.cursor()
            cursor.execute("UPDATE USER SET "+field+" = %s WHERE USER_ID = %s;",(newValue,user))
            connection.commit()
        finally:
            connection.close()
            
            
def main():
    userDao = UserDAO()
    x = userDao.get("root", "federico")
    print(x)
    print(x[0][0])
    print (x[0][1])
    
if __name__ == '__main__':
    main()