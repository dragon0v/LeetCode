from typing import *
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 双重循环，超时
        presum = [0]
        for n in nums:
            presum.append(presum[-1]+n)
        print(presum)

        n = len(nums)
        i,j = 0, 1
        res = n+10
        while i <= n:
            while nums[i]<=0:
                i += 1
            while j <= n and j-i<res:
                print(nums[i:j],presum[j] - presum[i])
                if presum[j] - presum[i] >= k:
                    # print(nums[i:j])
                    res = min(res,j-i)
                    i += 1
                    j = i+1
                else:
                    j += 1
            i += 1
            j = i+1

        return res if res <= n else -1

        



s = Solution()
t = s.shortestSubarray([-28,81,-20,28,-29],89)
print(t)