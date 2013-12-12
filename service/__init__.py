import MySQLdb

class DBConnector:
    
    def openConnection(self):
        return MySQLdb.connect(host='localhost', user='root',password='iamtheroot',db='OS_SQL')
