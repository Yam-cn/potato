'''
Created on 2017-01-06

@author: Chen
'''

from components.database.mongo import *

class AccountInfoDao():
    
    def __init__(self):
        self.AccountInfoDB = mongo_db(collection = "account_info").get_col()

    def addAccount(self,account):
        if type(account) is not dict:
            print 'the type of insert data isn\'t dict'             
            exit(0)
        self.AccountInfoDB.insert(account)
        account_id =account['account_id']
        #account_id = self.AccountInfoDB.insert_one(account).insert_id
        return account_id
        
    def updateAccount(self,accountId,account):
        self.AccountInfoDB.update({'account_id':accountId},{"$set":account})

    def getAccountByAccID(self,accountId):
        return self.AccountInfoDB.find({"account_id":accountId})

    def getAllAccount(self):
        return self.AccountInfoDB.find()
    
    def deleteAccountByAccID(self,accountId):
        return self.AccountInfoDB.remove({"account_id":accountId})
