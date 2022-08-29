from typing import *
from itertools import combinations
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        for i in range(3,len(nums)):
            tar = nums[i]
            for li in combinations(nums[:i],3):
                if sum(li)==tar:
                    res += 1
        return res
s = Solution()
t = s.countQuadruplets([1,2,3,4,6,8])
print(t)