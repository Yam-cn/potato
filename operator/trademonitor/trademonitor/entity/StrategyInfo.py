'''
Created on 2017-01-15

@author: Chen
'''
import uuid
import datetime

class StrategyInfo(object):
    '''
    classdocs
    '''

    def __init__(self, request):

        if request == None:
            return
        else:
            self.strategy_id = request.REQUEST.get("strategy_id","")
            self.strategy_name = request.REQUEST.get("strategy_name","")
            self.ticker= request.REQUEST.get("ticker","")
            self.position_lot = request.REQUEST.get("position_lot","")
            self.strategy_profit = request.REQUEST.get("strategy_profit","")
            self.position_profit = request.REQUEST.get("position_profit","")
            self.args = request.REQUEST.get("args","")
            self.account_id = request.REQUEST.get("account_id","")
            self.filename = request.REQUEST.get("filename","")
            self.status = request.REQUEST.get("status","")
            self.date = request.REQUEST.get("date","")

    def getStrategyInfoDict(self):
        dict = {}
        dict.update(self.__dict__)
        return dict


