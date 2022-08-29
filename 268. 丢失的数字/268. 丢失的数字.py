from typing import *
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exist = [False for _ in range(n+1)]
        for num in nums:
            exist[num] = True
        return exist.index(False)

s = Solution()
t = s.missingNumber([1,3,0])
print(t)