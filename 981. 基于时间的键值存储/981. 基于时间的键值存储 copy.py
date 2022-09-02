from bisect import bisect_left
from collections import defaultdict
class TimeMap:
    # 思路很简单，get时根据timestamp做一个二分查找，找到对应的value下标即可
    def __init__(self):
        self.d = defaultdict(list)  # 记录values
        self.t = defaultdict(list)  # 记录ts

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value])  # TODO 不加[]为什么会不行
        self.t[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        vals = self.d[key]
        if vals==[]:
            return ""
        ts = self.t[key]
        # print(vals)
        idx = bisect_left(ts,timestamp+1)-1
        if idx < 0:
            return ""
        return vals[idx][0]
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)