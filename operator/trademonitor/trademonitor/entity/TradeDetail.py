'''
Created on 2017-01-15

@author: Chen
'''
import uuid
import datetime

class TradeDetail(object):
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
            self.trade_price = request.REQUEST.get("trade_price","")
            self.trade_amount = request.REQUEST.get("trade_amount","")
            self.trade_datetime = request.REQUEST.get("trade_datetime","")

    def getTradeDetailDict(self):
        dict = {}
        dict.update(self.__dict__)
        return dict


