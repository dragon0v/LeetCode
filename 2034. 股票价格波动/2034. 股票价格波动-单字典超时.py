from collections import defaultdict
class StockPrice:
    # 超时
    def __init__(self):
        self.rec = defaultdict(int)  # ts:price
        self.maxkey = -1
        self.maxval = -1
        self.minval = 10e10

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.rec.keys():
            self.rec[timestamp] = price
            self.maxkey = max(timestamp,self.maxkey)
            self.maxval = max(self.rec.values())
            self.minval = min(self.rec.values())
        else:
            self.rec[timestamp] = price
            self.maxkey = max(timestamp,self.maxkey)
            self.maxval = max(self.maxval,price)
            self.minval = min(self.minval,price)

    def current(self) -> int:
        return self.rec[self.maxkey]

    def maximum(self) -> int:
        return self.maxval

    def minimum(self) -> int:
        return self.minval


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()