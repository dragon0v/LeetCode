class StockSpanner:
    # 单调栈
    def __init__(self):
        self.st = [(-1,100009)]  # 股票下标，股票价格
        self.idx = -1


    def next(self, price: int) -> int:
        # 调用 next 时，先将栈中价格小于等于此时 price 的元素都弹出，
        # 直到遇到一个大于 price 的值，并将 price 入栈，计算下标差返回。
        # print(self.st)
        self.idx += 1
        while price>=self.st[-1][1]:
            self.st.pop()
        self.st.append((self.idx,price))
        return self.idx - self.st[-2][0]




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)