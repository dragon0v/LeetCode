class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        s = 0
        for i in range(int(len(nums)/2)):
            s += nums[2*i]
        return s