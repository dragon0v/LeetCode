class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 数组循环方法
        
        # 优化3：只需使用一行数组，因为第一行和第一列全是1
        last = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                last[j] += last[j-1]
        return last[-1]


s = Solution()
t = s.uniquePaths(3,7)
print(t)