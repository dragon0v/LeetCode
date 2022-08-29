from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        presum = [0]
        for n in nums:
            presum.append(presum[-1]+n)
        print(presum)
        for i in range(len(presum)):
            for j in range(i+1,len(presum)):
                if presum[j]-presum[i]==k:
                    res += 1

        return res
# 超时
s = Solution().subarraySum([1,-1,0],0)
print(s)