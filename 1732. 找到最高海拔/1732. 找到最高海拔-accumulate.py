from itertools import accumulate
from typing import *


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 前缀和，无需数组，只需保留最大值和当前前缀和即可
        # accumulate一行实现
        return max(accumulate(gain))

s = Solution()
t = s.largestAltitude([2,3,4,5,5])
print(t)