from typing import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
s = Solution()
t = s.containsDuplicate([1,1,22])
print(t)