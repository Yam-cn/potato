# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 13:06:56 2015

@author: Eunice
"""

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from engine import bar
# 以上模块仅测试用
from engine.broker.fillstrategy import DefaultStrategy
from engine.broker.backtesting import TradePercentage
from engine import strategy
from engine.technical import ma
from engine.technical import cross

class thrSMA(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, short_l, mid_l, long_l, up_cum):
        strategy.BacktestingStrategy.__init__(self, feed)
        self.__instrument = instrument
        self.getBroker().setFillStrategy(DefaultStrategy(None))
        self.getBroker().setCommission(TradePercentage(0.001))
        self.__position = None
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__malength1 = int(short_l)
        self.__malength2 = int(mid_l)
        self.__malength3 = int(long_l)
        self.__circ = int(up_cum)

        self.__ma1 = ma.SMA(self.__prices, self.__malength1)
        self.__ma2 = ma.SMA(self.__prices, self.__malength2)
        self.__ma3 = ma.SMA(self.__prices, self.__malength3)

    def getPrice(self):
        return self.__prices

    def getSMA(self):
        return self.__ma1,self.__ma2, self.__ma3

    def onEnterCanceled(self, position):
        self.__position = None

    def onEnterOK(self):
        pass

    def onExitOk(self, position):
        self.__position = None
        #self.info("long close")

    def onExitCanceled(self, position):
        self.__position.exitMarket()

    def buyCon1(self):
        if cross.cross_above(self.__ma1, self.__ma2) > 0:
            return True

    def buyCon2(self):
        m1 = 0
        m2 = 0
        for i in range(self.__circ):
            if self.__ma1[-i-1] > self.__ma3[-i-1]:
                m1 += 1
            if self.__ma2[-i-1] > self.__ma3[-i-1]:
                m2 += 1

        if m1 >= self.__circ and m2 >= self.__circ:
            return True

    def sellCon1(self):
        if cross.cross_below(self.__ma1, self.__ma2) > 0:
            return True


    def onBars(self, bars):
        # If a position was not opened, check if we should enter a long position.

        if self.__ma2[-1]is None:
            return

        if self.__position is not None:
            if not self.__position.exitActive() and cross.cross_below(self.__ma1, self.__ma2) > 0:
                self.__position.exitMarket()
                #self.info("sell %s" % (bars.getDateTime()))

        if self.__position is None:
            if self.buyCon1() and self.buyCon2():
                shares = int(self.getBroker().getCash() * 0.2 / bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument, shares)
                print bars[self.__instrument].getDateTime(), bars[self.__instrument].getPrice()
                #self.info("buy %s" % (bars.getDateTime()))


def testStrategy():
    from engine import bar

    strat = thrSMA
    instrument = '600288'
    market = 'SH'
    fromDate = '20150101'
    toDate ='20150601'
    frequency = bar.Frequency.MINUTE
    paras = [2, 20, 60, 10]
    plot = True

    #############################################path set ############################33
    import os
    print os.path.split(os.path.realpath(__file__))
    if frequency == bar.Frequency.MINUTE:
        path = os.path.join(os.environ.get('STRATEGYPATH'), '..', 'histdata', 'minute')
    elif frequency == bar.Frequency.DAY:
        path = os.path.join(os.environ.get('STRATEGYPATH'), '..', 'histdata', 'day')
    filepath = os.path.join(path, instrument + market + ".csv")


    #############################################don't change ############################33
    from engine.barfeed.csvfeed import Feed

    barfeed = Feed(frequency)
    barfeed.setDateTimeFormat('%Y-%m-%d %H:%M:%S')
    barfeed.loadBars(instrument, market, fromDate, toDate, filepath)

    engine_id = instrument + '.' + market
    strat = strat(barfeed, engine_id, *paras)

    from engine.stratanalyzer import returns
    from engine.stratanalyzer import sharpe
    from engine.stratanalyzer import drawdown
    from engine.stratanalyzer import trades

    retAnalyzer = returns.Returns()
    strat.attachAnalyzer(retAnalyzer)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    strat.attachAnalyzer(sharpeRatioAnalyzer)
    drawDownAnalyzer = drawdown.DrawDown()
    strat.attachAnalyzer(drawDownAnalyzer)
    tradesAnalyzer = trades.Trades()
    strat.attachAnalyzer(tradesAnalyzer)

    strat.run()


    #夏普率
    sharp = sharpeRatioAnalyzer.getSharpeRatio(0.05)
    #最大回撤
    maxdd = drawDownAnalyzer.getMaxDrawDown()
    #收益率
    return_ = retAnalyzer.getCumulativeReturns()[-1]
    #收益曲线
    return_list = []
    for item in retAnalyzer.getCumulativeReturns():
        return_list.append(item)


def run_strategy(ticker, account_id, paras):
    print ticker
    print account_id
    print paras

    strat = testStrategy()

if __name__ == "__main__":
    testStrategy()
