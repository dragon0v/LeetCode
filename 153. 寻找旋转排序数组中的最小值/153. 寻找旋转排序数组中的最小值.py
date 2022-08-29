class Solution:
    def findMin(self, nums) -> int:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return nums[i+1]
        return nums[0]

# 简单题这样做，时间复杂度On
# 但这题是中等题，就应该想一个Ologn的解法
