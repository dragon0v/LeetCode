from math import inf


class MinStack:
    # 能在常数时间内检索到最小元素的栈
    # 错误解，无法AC
    def __init__(self):
        self.m = inf
        self.pos = -1
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if val<self.m:
            self.pos = len(self.st)-1
            self.m = val

    def pop(self) -> None:
        self.top(pop=True)

    def top(self,pop=False) -> int:
        if len(self.st)-1 == self.pos:
            self.m = self.st[0]
            self.pos = 0
            for i,v in enumerate(self.st[:-1]):
                if v<self.m:
                    self.m = v
                    self.pos = i
        # print(self.st,self.m,self.pos)
        if pop:
            return self.st.pop()
        return self.st[-1]

    def getMin(self) -> int:
        return self.m



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]