class Solution:
    def searchRange(self, nums, target: int):
        i = 0
        j = len(nums)-1
        while i<=j:
            k = (i+j)//2
            if nums[k] == target:
                #
                pass
            elif nums[k] > target:
                j = k - 1
            else:
                i = k + 1
        return [-1,-1]
        
# Ologn 先对分找位置，然后顺序？