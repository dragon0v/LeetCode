class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 数组循环方法
        
        # 优化2：每次更新matrix实际上只用到本行和上一行的信息，改为只使用两行数组
        last = [1]*n
        now = [1] + [0]*(n-1)
        for i in range(1,m):
            for j in range(1,n):
                now[j] = last[j] + now[j-1]
            last = now[:]
        return now[-1]


s = Solution()
t = s.uniquePaths(3,7)
print(t)