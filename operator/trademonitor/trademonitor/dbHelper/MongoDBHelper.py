'''
Created on 2016-8-14

@author: kanyuan
'''
from pymongo import MongoClient


class MongoDBHelper(object):
    
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['potatodb']
    
    def getAccountInfoDB(self):
        return self.db.account_info
        
    def getStrategyInfoDB(self):
        return self.db.strategy_info
        
    
    def getTradeDetailDB(self):
        return self.db.trade_detail