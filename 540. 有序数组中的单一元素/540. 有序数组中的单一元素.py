from typing import *

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 思路：对分，因为出现次数不是2就是1，
        # 对分时比较中间元素与左右是否相同，都不相同则返回这个元素，
        # 中=右，此时是正常情况，说明1在右边
        # 中=左，此时说明1在左边
        if len(nums)==1 or nums[0] != nums[1]:
            return nums[0]
        i = 0
        j = len(nums)-1
        while i<=j:
            k = (i+j)//2
            # 保证k是双数
            if k % 2 == 1:
                k += 1
                
            if (k+1 > len(nums)-1) or (nums[k] != nums[k-1] and nums[k] != nums[k+1]):
                return nums[k]
            if nums[k] == nums[k+1]:
                i = k
            elif nums[k] == nums[k-1]:
                j = k

        
        
s = Solution()
t = s.singleNonDuplicate([0,5,5,6,6,9,9])
print(t)