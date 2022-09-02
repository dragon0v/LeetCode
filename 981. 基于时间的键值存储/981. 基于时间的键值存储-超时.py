from bisect import bisect_left
from collections import defaultdict
class TimeMap:
    # 思路很简单，get时根据timestamp做一个二分查找，找到对应的value下标即可
    # 超时了，应该是ts的构造那
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        vals = self.d[key]
        if vals==[]:
            return ""
        ts = [v[1] for v in vals]
        print(vals)
        idx = bisect_left(ts,timestamp+1)-1
        if idx<0:
            return ""
        return vals[idx][0]
        




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)