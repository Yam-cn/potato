'''
Created on 2017-01-15

@author: Chen
'''
import uuid
import datetime

class AccountInfo(object):
    '''
    classdocs
    '''

    def __init__(self, request):

        if request == None:
            return
        else:
            self.account_id = request.REQUEST.get("account_id","")
            self.account_type = request.REQUEST.get("account_type","")
            self.dyn_right= request.REQUEST.get("dyn_right","")
            self.cash_avalible=request.REQUEST.get("cash_avalible","")
            self.cash_frozen = request.REQUEST.get("cash_frozen","")
            self.asset = request.REQUEST.get("asset","")
            self.date = request.REQUEST.get("date","")

    def getAccountInfoDict(self):
        dict = {}
        dict.update(self.__dict__)
        return dict


