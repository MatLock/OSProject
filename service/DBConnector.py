'''
Created on 09/12/2013

@author: matlock
'''


import MySQLdb


class DBConnector:
    
    def openConnection(self):
        return MySQLdb.Connect(host='localhost',user='root',passwd='iamtheroot',db='OS_SQL')