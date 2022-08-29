from lib2to3.pgen2.token import MINUS
from math import inf
from typing import *
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            maxnum = minnum = nums[i]
            for j in range(i,len(nums)):
                maxnum = max(maxnum,nums[j])
                minnum = min(minnum,nums[j])
                res += maxnum-minnum
        return res

# 3700ms

s = Solution().subArrayRanges([1,2,3,3,3,3,2,1,4])
print(s)