class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        if len(nums)==1:
            return res
        i,j = 0,0
        crt = nums[0]
        while j<len(nums)-1:
            if nums[j+1] > nums[j]:
                j += 1
                crt += nums[j]
            else:
                res = max(res,crt)
                i = j+1  # j是提前看的，所以是j+1
                j += 1
                crt = nums[i]
        
        return max(crt,res)