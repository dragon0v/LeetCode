class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            k = (i+j)//2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                j = k - 1
            else:
                i = k + 1
                
        # 完全就是对分查找，只是找不到的情况返回i就行了
        return i
