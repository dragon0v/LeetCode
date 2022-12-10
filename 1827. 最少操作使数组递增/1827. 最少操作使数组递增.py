class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return 0
        last = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if nums[i]<=last:
                res += last-nums[i]+1
                last += 1
            else:
                last = nums[i]
        return res
