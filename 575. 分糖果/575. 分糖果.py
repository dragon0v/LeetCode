from typing import *
from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # 这里用counter其实是为了获取到种类数目，所以就没必要使用counter，直接用set即可
        c = Counter(candyType)
        types = list(c.values())
        types.sort(reverse=True)
        s = sum(types)
        girl = 0
        res = 0
        for each in types:
            girl += each
            if girl <= s:
                res += 1
            else:
                return res
        return min(res,s//2)

s = Solution()
t = s.distributeCandies([1,1,1,2,3,1])
print(t)
