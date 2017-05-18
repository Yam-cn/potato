# -*- coding: utf-8 -*-
"""
# Copyright 2011-2016 Zhixiong Ge
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Created on Sun Dec 11 14:31:04 2016
"""

import pymongo

from engine.utils.configure import getMongoInfo

class DbHandler(object):
    def __init__(self):
        mongo_info = getMongoInfo()
        self.__mongo = pymongo.MongoClient(host=mongo_info['host'],
                                           port=mongo_info['port'])

    def getAccountLogin(self, usrid):
        return self.__mongo.tradedb.account_info.find_one({'userid': usrid})

    def updateAccountBal(self, usr_id, balance, cash_frozen, cash_avail, margin, dt):
        """

        :param usr_id: 账户id
        :param balance: 动态权益
        :param cash_frozen: 可用资金
        :param cash_avail: 冻结资金
        :param margin: 资产
        :param dt: 日期

        :return:
        """

        doc = {'usrid': usr_id,
               'balance': balance,
               'cash_frozen': cash_frozen,
               'cash_avail': cash_avail,
               'margin': margin,
               'datetime': dt}
        return self.__mongo.tradedb.account_balance.find_one_and_replace({'usrid': usr_id}, doc)

    def updateStrategyInfo(self, strategy_id, asset, volume, profit, unrealised_profit, usrid, dt):
        """

        :param strategy_id: 策略id
        :param asset: 交易品种
        :param volume: 持仓数量
        :param profit: 策略盈亏
        :param unrealised_profit: 持仓盈亏
        :param usrid: 账户id
        :param dt: 日期
        :return:
        """
        doc = {'strategy_id': strategy_id,
               'asset': asset,
               'volume': volume,
               'profit': profit,
               'unrealised_profit': unrealised_profit,
               'usrid': usrid,
               'dt': dt}
        self.__mongo.tradedb.strategy_info.find_one_and_replace({'strategy_id': strategy_id}, doc)

    def addTrade(self, strategy_id, asset, fill_price, volume, dt):
        """

        :param strategy_id:策略id
        :param asset:交易品种
        :param fill_price:成交点位
        :param volume:成交量
        :param dt: 成交时间
        :return:
        """
        doc = {'strategy_id': strategy_id,
               'asset': asset,
               'volume': volume,
               'fill_price': fill_price,
               'dt': dt}

        self.__mongo.tradedb.trades.insert_one(doc)
