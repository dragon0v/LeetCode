class Solution:
    def maxSubArray(self, nums) -> int:
        i,j = 0,0
        maxsum = -11111
        crtsum = 0
        while j<len(nums):
            crtsum += nums[j]
            maxsum = max(maxsum,crtsum)
            j+=1
            if xxx:
                i = j
                crtsum = 0