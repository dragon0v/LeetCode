class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # 0,0,3,4,4
        nums.sort()
        n = len(nums)
        if nums[0]>=n:
            return n
        for i in range(1,n):
            # n-i是大于等于nums[i-1]数的数量
            if n-i>nums[i-1] and nums[i]>=n-i:
                return n-i
        return -1