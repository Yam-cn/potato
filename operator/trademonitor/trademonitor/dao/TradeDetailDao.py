'''
Created on 2017-01-06

@author: Chen
'''
from trademonitor.dbHelper.MongoDBHelper import *

class TradeDetailDao():
    def __init__(self):
        mongoDBHelper = MongoDBHelper()
        self.TradeDetailDB = mongoDBHelper.getTradeDetailDB()
    
    def addTradeDetail(self,tradedetail):
        if type(tradedetail) is not dict:
            print 'the type of insert data isn\'t dict'             
            exit(0)
        self.TradeDetailDB.insert(tradedetail)

    def getAllTradeDetail(self):
        return self.TradeDetailDB.find().limit(20)

    def getTradeDetailByID(self,strategy_id):
        return self.TradeDetailDB.find({"strategy_id":strategy_id})

    def getTradeDetailByIDList(self,strategyidarray):
        return self.TradeDetailDB.find({"strategy_id":{"$in":strategyidarray}})

    def deleteTradeDetail(self,strategy_id):
        return self.TradeDetailDB.remove({"strategy_id":strategy_id})

    def updateTradeDetail(self,strategy_id,detail):
        self.TradeDetailDB.update({'strategy_id':strategy_id},{"$set":detail},upsert = False)