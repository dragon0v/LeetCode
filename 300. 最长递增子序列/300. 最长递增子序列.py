class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 经典题，
        # 思路：动态规划，dp[i] = max(dp[j])+1, j<i and nums[i]>nums[j]
        # 复杂度n^2
        dp = [1 for _ in nums]
        for i in range(1,len(nums)):
            dp[i] = max([dp[j] if nums[i]>nums[j] else 0 for j in range(i)]) + 1  # 0很巧妙，将dp[i]还原成1
        print(dp)
        return max(dp)