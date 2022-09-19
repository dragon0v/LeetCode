from typing import *
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        c = Counter(nums)
        # print(c)
        ans = []
        for k,v in c.most_common(len(nums)):
            for i in range(v):
                ans.append(k)
        
        return ans[::-1]