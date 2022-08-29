from typing import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for n in nums:
            if n in a:
                return True
            a.add(n)
        return False
s = Solution()
t = s.containsDuplicate([1,1,22])
print(t)