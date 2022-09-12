from heapq import heappush, heappop
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 枚举每一位能成为ratio最高的工人，找ratio和quality最低的k名工人
        n = len(quality)
        ratio = [x/y for x,y in zip(wage,quality)]
        pairs = sorted(zip(quality,wage,ratio),key=lambda x:x[2])
        sumq = 0
        h = []
        for i in range(k-1):
            sumq += pairs[i][0]
            heappush(h,-pairs[i][0])

        res = 10**9
        for i in range(n-k+1):
            # 枚举能成为ratio最高的工人
            cr = pairs[k-1+i][2]  # current ratio
            cq = pairs[k-1+i][0]  # current quality
            # 找quality最少的k个工人
            sumq += cq
            heappush(h,-cq)
            res = min(res,cr*sumq)
            sumq += heappop(h)
        return res
