from typing import *
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (1+n)*n//2-sum(nums)

s = Solution()
t = s.missingNumber([1,3,0])
print(t)