from collections import OrderedDict, defaultdict
from sortedcontainers import SortedList
class StockPrice:
    # 对于储存，最值，最后时间戳三个任务分别使用三种数据结构储存
    def __init__(self):
        self.rec = defaultdict(int)  # ts:price
        self.prices = SortedList()  # 存放价格
        self.maxkey = -1  # 最后的ts

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.rec:
            self.prices.discard(self.rec[timestamp])
        self.rec[timestamp] = price
        self.prices.add(price)
        self.maxkey = max(self.maxkey, timestamp)

    def current(self) -> int:
        return self.rec[self.maxkey]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()