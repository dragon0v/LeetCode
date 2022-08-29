from math import ceil
from typing import *
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 二分查找
        # print(ceil(4444/2220))
        def cost(speed):
            return sum(ceil(pile/speed) for pile in piles)

        i,j = 1,max(piles)
        while i<j:
            k = (i+j)//2
            print(i,j,k)
            if cost(k)>h:
                i = k + 1
            else:
                j = k
        return i  # 为什么是i？


s = Solution()
t = s.minEatingSpeed([1,2,3,4444],5)
print(t)