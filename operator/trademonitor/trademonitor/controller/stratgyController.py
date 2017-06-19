'''
Created on 2016-8-6

@author: Chen
'''
from django.http import HttpResponse  
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import traceback
from trademonitor.decorator.Ajax import *
from trademonitor.dao.AccountInfoDao import *
from trademonitor.dao.StrategyInfoDao import *
from trademonitor.dao.TradeDetailDao import *
from trademonitor.entity.AccountInfo import *
from trademonitor.entity.StrategyInfo import *
from trademonitor.entity.TradeDetail import *
from components.celery.tasks import *
from components.celery.tasksmgmt import *

def strategy(request):

    return render_to_response('stratrgies.html', locals())

@csrf_exempt
@Ajax
def addAccount(request):
    accdao = AccountInfoDao()
    oAccountInfo = AccountInfo(request)
    AccountInfoDict = oAccountInfo.getAccountInfoDict()

    account_id = request.REQUEST.get('account_id','')
    if not isAccountExisted(account_id):
        accdao.addAccount(AccountInfoDict)
    else:
        accdao.updateAccount(account_id, AccountInfoDict)
        account_id = 1
    rlist = []
    rlist.append(account_id)
    return rlist

@csrf_exempt
@Ajax
def queryAllAccount(request):
    accdao = AccountInfoDao()
    result = accdao.getAllAccount()
    rlist = []
    for acc in result:
        rdict = acc
        rdict.pop('_id')
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def queryAccount(request):
    account_id = request.REQUEST.get('account_id','')
    accdao = AccountInfoDao()
    result = accdao.getAccountByAccID(account_id)
    rlist = []
    for acc in result:
        rdict = acc
        rdict.pop('_id')
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def deleteAccount(request):
    account_id = request.REQUEST.get('account_id','')
    if account_id == '':
        return 0
    accdao = AccountInfoDao()
    if isAccountExisted(account_id):
        accdao.deleteAccountByAccID(account_id)
    rlist = []
    rlist.append(account_id)
    return rlist

@csrf_exempt
@Ajax
def addStrategy(request):
    strdao = StrategyInfoDao()
    oStrategyInfo = StrategyInfo(request)
    StrategyInfoDict = oStrategyInfo.getStrategyInfoDict()

    strategy_id = request.REQUEST.get('strategy_id','')
    if not isStrategyExisted(strategy_id):
        strdao.addStrategy(StrategyInfoDict)
    else:
        strdao.updateStrategy(strategy_id, StrategyInfoDict)
    print "--==Running the strategy==--"
    ticker = request.REQUEST.get('ticker','')
    account_id = request.REQUEST.get('account_id','')
    algo_fname = request.REQUEST.get('filename','')
    args = request.REQUEST.get('args','')
    task = runAlgo.delay(ticker, account_id, algo_fname, args)
    add_task(strategy_id, task.id)
    print 'Task is running'

    return strategy_id

@csrf_exempt
@Ajax
def stopStrategy(request):
    strategyid = request.REQUEST.get('strategy_id','')
    rlist = []
    if strategyid == '':
        rlist.append(0)
        return rlist
    print "--==Stopping the strategy==--"
    stop_task(strategyid)

    rlist.append(strategyid)
    return rlist

@csrf_exempt
@Ajax
def queryStrategy(request):
    strategy_id = request.REQUEST.get('strategy_id','')
    if strategy_id == '':
        return 0
    strdao = StrategyInfoDao()
    result = strdao.getStrategyByID(strategy_id)
    rlist = []
    for str in result:
        rdict = str
        rdict.pop('_id')
        try:
            rdict['status'] = get_task_status(strategy_id)
        except Exception, e:
            pass
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def queryAllStrategy(request):
    strdao = StrategyInfoDao()
    result = strdao.getAllStrategy()
    rlist = []
    for item in result:
        rdict = item
        rdict.pop('_id')
        #ISOTIMEFORMAT=u'%Y-%m-%d %X'
        #rdict['date'] = time.strftime(ISOTIMEFORMAT, time.localtime() )
        try:
            rdict['status'] = get_task_status(rdict["strategy_id"])
        except Exception, e:
            print e
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def deleteStrategy(request):
    strategyid = request.REQUEST.get('strategy_id','')
    if strategyid == '':
        return 0
    strdao = StrategyInfoDao()
    if isStrategyExisted(strategyid):
        strdao.deleteStrategyID(strategyid)
    remove_task(strategyid)
    rlist = []
    rlist.append(strategyid)
    return rlist

@csrf_exempt
@Ajax
def addTradeDetail(request):
    detaildao = TradeDetailDao()
    oTradeDetail = TradeDetail(request)
    TradeDetailDict = oTradeDetail.getTradeDetailDict()

    strategy_id = request.REQUEST.get('strategy_id','')
    detaildao.addTradeDetail(TradeDetailDict)
    #if not isTradeDetailExisted(strategy_id):
    #    detaildao.addTradeDetail(TradeDetailDict)
    #else:
    #    detaildao.updateTradeDetail(strategy_id, TradeDetailDict)

    return strategy_id

@csrf_exempt
@Ajax
def deleteTradeDetail(request):
    strategyid = request.REQUEST.get('strategy_id','')
    if strategyid == '':
        return 0
    detaildao = TradeDetailDao()
    if isTradeDetailExisted(strategyid):
        detaildao.deleteTradeDetail(strategyid)
    return strategyid

@csrf_exempt
@Ajax
def queryTradeDetail(request):
    strategy_id = request.REQUEST.get('strategy_id','')
    if strategy_id == '':
        return 0
    detaildao = TradeDetailDao()
    result = detaildao.getTradeDetailByID(strategy_id)
    rlist = []
    for detail in result:
        rdict = detail
        rdict.pop('_id')
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def queryAllTradeDetail(request):
    detaildao = TradeDetailDao()
    result = detaildao.getAllTradeDetail()
    rlist = []
    for detail in result:
        rdict = detail
        rdict.pop('_id')
        rlist.append(rdict)
    return rlist

@csrf_exempt
@Ajax
def queryStrategyStatus(request):
    rlist = []
    strategy_id = request.REQUEST.get('strategy_id','')
    if strategy_id == '':
        rlist.append('')
        return rlist
    try:
        rlist.append(get_task_status(strategy_id))
    except Exception, e:
        rlist.append('')
    return rlist

def isAccountExisted(account_id):
    accdao = AccountInfoDao()
    account = accdao.getAccountByAccID(account_id)
    if not account or account.count() == 0:
        return False
    else:
        return True

def isStrategyExisted(strategy_id):
    strdao = StrategyInfoDao()
    strategy = strdao.getStrategyByID(strategy_id)
    if not strategy or strategy.count() == 0:
        return False
    else:
        return True

def isTradeDetailExisted(strategy_id):
    detaildao = TradeDetailDao()
    detail = detaildao.getTradeDetailByID(strategy_id)
    if not detail or detail.count() == 0:
        return False
    else:
        return True
