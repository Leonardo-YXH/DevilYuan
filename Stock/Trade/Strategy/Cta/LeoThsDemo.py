# -*- coding:utf-8 -*-
"""
@author: leonardo
@created time: 2020-04-11
@last modified time:2020-04-11
"""
from ..DyStockCtaTemplate import *


class LeoThsDemo(DyStockCtaTemplate):
    name = 'LeoThsDemo'
    chName = '同花顺下单测试'

    backTestingMode = 'bar1m'

    broker = 'ths'
    # 策略实盘参数
    codes = ['600438.SH', '600386.SH', '300261.SZ']

    def __init__(self, ctaEngine, info, state, strategyParam=None):
        super().__init__(ctaEngine, info, state, strategyParam)

        self.has_sell = False

    def _onOpenConfig(self):
        myPos=self.ctaEngine.getCurPos(self)
        self._monitoredStocks.extend(self.codes)

    def _curInit(self, date=None):
        pass

    @DyStockCtaTemplate.onOpenWrapper
    def onOpen(self, date, codes=None):
        # 当日初始化
        self._curInit(date)

        self._onOpenConfig()

        # super().onOpen(date,codes)
        return True

    def onTicks(self, ticks):
        """
            收到行情TICKs推送
            @ticks: {code: DyStockCtaTickData}
        """
        print('on ticks')
        myPos = self.ctaEngine.getCurPos(self)
        print(myPos)
        # for t_code in ticks:
        #     tick = ticks[t_code]
        #     if t_code == '600438.SH':
        #         pass
        #         # self.buy(tick, 100, price=price)
        #     elif t_code == '300261.SZ':
        #         if datetime.now().minute % 2 == 0:
        #             entrust=self.sell(tick, 100,force=True)
        #             self.has_sell = True
        #             print('sell:{}'.format(entrust))
        #         else:
        #             self.has_sell=False

    def onBars(self, bars):
        price = 11.31

        for t_code in bars:
            price += 0.1
            tick = bars[t_code]
            if t_code == '600438.SH':
                pass
                # self.buy(tick, 100, price=price)
            elif t_code == '300261.SZ' and datetime.now().minute % 2 == 0:
                self.sell(tick, 100)
                self.has_sell = True
                print('--------------')