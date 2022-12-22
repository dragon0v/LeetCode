class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 没有原地要求是送分题
        return [nums[nums[i]] for i in range(len(nums))]