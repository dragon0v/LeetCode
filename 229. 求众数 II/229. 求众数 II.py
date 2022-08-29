from collections import Counter
from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        n = len(nums)
        for num,value in c.items():
            if value > n//3:
                res.append(num)
        return res

# 这个就是为了过每日一题，根本不算什么解法
# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

s = Solution().majorityElement([1,2,3,4,3])
print(s)