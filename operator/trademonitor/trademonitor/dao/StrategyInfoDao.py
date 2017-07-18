'''
Created on 2017-01-06

@author: Chen
'''
from components.database.mongo import *

class StrategyInfoDao():

    def __init__(self):
        self.StrategyInfoDB = mongo_db(collection = "strategy_info").get_col()

    def addStrategy(self,strategy):
        self.StrategyInfoDB.insert(strategy)
        return strategy["strategy_id"]

    def getAllStrategy(self):
        return self.StrategyInfoDB.find()

    def getStrategyByID(self,strategy_id):
        return self.StrategyInfoDB.find({"strategy_id":strategy_id})

    def getStrategyByAccID(self,account_id):
        return self.StrategyInfoDB.find({"account_id":account_id})

    def getStrategyByAccIDArray(self,accountidarray):
        return self.StrategyInfoDB.find({"account_id":{"$in":accountidarray}})

    def deleteStrategyID(self,strategy_id):
        return self.StrategyInfoDB.remove({"strategy_id":strategy_id})

    def updateStrategy(self,strategy_id,strategy):
        self.StrategyInfoDB.update({'strategy_id':strategy_id},{"$set":strategy},upsert = False)

    def stopStrategy(self,strategy_id):
        self.StrategyInfoDB.update({'strategy_id':strategy_id},{"$set":{"status":"0"}},upsert = False)
