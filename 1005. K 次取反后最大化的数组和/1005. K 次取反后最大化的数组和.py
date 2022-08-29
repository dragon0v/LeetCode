from typing import *
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        n = len(nums)
        # 优先翻转最小的负数，翻转完所有负数如果次数还不到k
        # 若k是偶数，则直接返回sum，若k是奇数，则翻转当前最小的数
        for i,v in enumerate(nums):
            if v<0:
                k-=1
                nums[i] = -nums[i]
            else:
                break
            if k==0:
                break
        
        return sum(nums) if k%2==0 else sum(nums)-min(nums)*2

s = Solution().largestSumAfterKNegations([-1,2,-3,-4],2)
print(s)