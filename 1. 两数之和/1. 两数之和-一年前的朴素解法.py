class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            another=target-nums[i]
            if another in nums[i+1:]:
                j=nums[i+1:].index(another)
                return [i,j+i+1]