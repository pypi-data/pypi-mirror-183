# 策略
import time
import datetime
from strategy_api.strategies.template import StrategyTemplate
from strategy_api.tm_api.Binance.futureUsdt import BinanceFutureUsdtGateway
from strategy_api.tm_api.Binance.futureInverse import BinanceFutureInverseGateway
from strategy_api.tm_api.object import Interval, BarData, OrderData, Status, PositionSide


# 策略类
class StrategyDemo(StrategyTemplate):
    # 属性 作者(标志该策略的开发人员)
    author = "DYX"

    # 属性 设置链接网关需要的参数参数
    api_setting = {
        "key": "HdEhFjmn21Gbew3awhR75efLKyqtSNoHwTQJByjwB7TuaISWS6vTwqlQ9oB4NVtg",
        "secret": "w1qascqJBDHisjmvimQKbIgjABAo3Er8ji9Dn81IEdNOAOxXN77D5GHjxI0hBjHK",
        "proxy_host": "127.0.0.1",
        "proxy_port": 8010,
    }

    # 初始化方法
    def __init__(self, gate_way, symbol: str, interval: Interval, tick_nums: int):
        super(StrategyDemo, self).__init__(gate_way, symbol, interval, tick_nums)

    # 初始化策略参数
    def init_parameters(self):
        self.buy_switch = True
        self.long_id = ""
        self.short_id = ""
        self.volume = 1
        self.rate_stop = 0.01

    # k 线数据的回调, 可以在该方法里面记录 k 线数据、分析k线数据
    def on_bar(self, bar: BarData):
        if self.buy_switch:
            # 开多单
            self.long_id = self.api.buy(symbol=self.symbol, volume=self.volume, price=10, maker=False, position_side=PositionSide.TWOWAY)
            # 开空单
            self.short_id = self.api.short(symbol=self.symbol, volume=self.volume, price=10, maker=False, position_side=PositionSide.TWOWAY)
            self.buy_switch = False


    # 计算 止盈止损
    def calculate_profit_loss(self, order_time: datetime):
        pass

    # 订单 数据的回调，订单状态的改变都会通过websoket 推送到这里，例如 从提交状态 改为 全成交状态，或者提交状态 改为 撤销状态 都会推送
    # 可以在这里对仓位进行一个记录
    def on_order(self, order: OrderData):
        if order.status == Status.ALLTRADED and self.long_id == order.orderid:
            print("多单全部成交")
            # self.api.sell(symbol=self.symbol, volume=self.volume, price=round(order.traded_price * (1-self.rate_stop), 3),  stop_loss=True)
            pass
        elif order.status == Status.ALLTRADED and self.short_id == order.orderid:
            print("空单全部成交")
            # self.api.sell(symbol=self.symbol, volume=self.volume, price=round(order.traded_price * (1+self.rate_stop), 3),  stop_loss=True)
            pass

def start_strategy():
    s = StrategyDemo(gate_way=BinanceFutureInverseGateway(), symbol="BTCUSD_PERP", interval=Interval.MINUTE,
                     tick_nums=200)
    s.start()
    print("策略运行中")
    while True:
        time.sleep(10)


if __name__ == '__main__':
    print("启动量化系统: 等待策略运行")
    start_strategy()
