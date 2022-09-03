from typing import *
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        if len(nums)<3:
            return False
        for i in range(len(nums)-1):
            ss = nums[i] + nums[i+1]
            if ss in s:
                return True
            s.add(ss)
        
        return False