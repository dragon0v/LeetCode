from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=2:
            return []
        nums.sort()
        n = len(nums)
        res = []
        print(nums)
        for i,v in enumerate(nums):
            j = i + 1
            k = n - 1
            while j<k:
                if nums[j]+nums[k] == -v:
                    # TODO 去重可以优化吧，目前3900ms7%
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    # 可能还有其他和为-v的解，需要继续不能break
                    k -= 1
                    j += 1
                elif nums[j]+nums[k] > -v:
                    k -= 1
                else:
                    j += 1
        
        return res
s = Solution()
t = s.threeSum([1,2,3,4,5,6,2,3,4,6,5,-10,-1,-1,-4,0,1])
print(t)
