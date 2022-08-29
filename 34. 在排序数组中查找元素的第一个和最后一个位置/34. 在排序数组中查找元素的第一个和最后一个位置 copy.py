class Solution:
    def searchRange(self, nums, target: int):
        i = -1
        j = -1
        for k,v in enumerate(nums):
            if v == target and i == -1:
                i = k
            if v > target:
                if i == -1:
                    return [-1,-1]
                else:
                    return [i,k-1]
        if i != -1:
            return [i,len(nums)-1]
        else:
            return [-1,-1]
        
