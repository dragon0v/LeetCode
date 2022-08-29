class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        # 动态规划
        # 根据官方java版翻译
        s = sum(nums)
        diff = s-target
        if diff<0 or diff%2!=0:
            return 0
        n = len(nums)
        neg = diff//2
        dp = [[0]*(neg+1) for _ in range(n+1)]
        dp[0][0] = 1
        print(dp)
        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j]
                if j>=num:
                    dp[i][j] += dp[i-1][j-num]
                    
        return dp[n][neg]
        

s = Solution()
t = s.findTargetSumWays([1,1,1,1,1],3)
print(t)