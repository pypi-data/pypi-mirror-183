# 策略
import time
import datetime
from strategy_api.strategies.template import StrategyTemplate
from strategy_api.tm_api.Binance.futureUsdt import BinanceFutureUsdtGateway
from strategy_api.tm_api.Binance.futureInverse import BinanceFutureInverseGateway
from strategy_api.tm_api.object import Interval, BarData, OrderData, Status, PositionSide, DataType


# 策略类
class StrategyDemo(StrategyTemplate):
    # 属性 作者(标志该策略的开发人员)
    author = "DYX"

    # 属性 设置链接网关需要的参数参数
    api_setting = {
        "key": "",
        "secret": "",
        "proxy_host": "",
        "proxy_port": 0,
    }

    # 初始化方法
    def __init__(self, tick_nums: int = 0):
        super(StrategyDemo, self).__init__(tick_nums)

    # 初始化策略参数
    def init_parameters(self):
        self.buy_switch = True
        self.long_id = ""
        self.short_id = ""
        self.volume = 1
        self.rate_stop = 0.01

    # k 线数据的回调, 可以在该方法里面记录 k 线数据、分析k线数据
    def on_bar(self, bar: BarData):
        print(bar)
        if self.buy_switch:
            # 开多单
            self.long_id = self.get_gateway("Binance_inverse").buy(symbol="BTCUSD_PERP", volume=self.volume, price=10,
                                                                   maker=False, position_side=PositionSide.TWOWAY)
            # 开空单
            self.short_id = self.get_gateway("Binance_inverse").short(symbol="BTCUSD_PERP", volume=self.volume,
                                                                      price=10, maker=False,
                                                                      position_side=PositionSide.TWOWAY)
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
    # 初始化策略
    s = StrategyDemo()
    # 添加网关
    # 币本位网关
    inverse_gateway = s.add_gateway(BinanceFutureInverseGateway, "Binance_inverse")
    # U本位网关
    usdt_gateway = s.add_gateway(BinanceFutureUsdtGateway, "Binance_usdt")
    # 订阅数据
    usdt_gateway.subscribe(symbol="BTCUSDT", data_type=DataType.BAR, interval=Interval.MINUTE)

    print("策略运行中")
    while True:
        time.sleep(10)


if __name__ == '__main__':
    print("启动量化系统: 等待策略运行")
    start_strategy()
