class Solution:
    def climbStairs(self, n: int):
        # 动态规划 dp[i+2] = dp[i+1] + dp[i]
        a,b = 1,2
        if n<=2:
            return n
        for i in range(2,n):
            a,b = b,a+b
        return b