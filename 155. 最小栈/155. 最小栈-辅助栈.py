from math import inf


class MinStack:
    # 能在常数时间内检索到最小元素的栈
    # 辅助栈，再来一个储存最小值的栈，和储存元素的栈同时操作
    def __init__(self):
        self.st = []
        self.mst = [inf]  # 栈顶储存当前的最小值

    def push(self, val: int) -> None:
        self.st.append(val)
        if val<self.mst[-1]:
            # 如果val是最小值,加入这个最小值
            self.mst.append(val)
        else:
            # 不是最小值，加入最小值
            self.mst.append(self.mst[-1])

    def pop(self) -> None:
        self.st.pop()
        self.mst.pop()

    def top(self,pop=False) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]