from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                res = max(res, min(height[i],height[j])*(j-i))
        return res
# 暴力，超时
s = Solution()
t = s.maxArea([1,8,6,2,5,4,8,3,7])
print(t)