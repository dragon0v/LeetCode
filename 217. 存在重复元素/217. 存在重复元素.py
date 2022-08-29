from typing import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        # 本质是哈希表
        return any(v>1 for v in c.values())

s = Solution()
t = s.containsDuplicate([1,1,22])
print(t)