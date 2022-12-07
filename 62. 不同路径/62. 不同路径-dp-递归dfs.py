from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 递归方法
        @ lru_cache(None)
        def dfs(i,j):
            if i==0 and j==0:
                return 1
            elif i==0:
                return dfs(i,j-1)
            elif j==0:
                return dfs(i-1,j)
            else:
                return dfs(i-1,j) + dfs(i,j-1)
        
        return dfs(m-1,n-1)

s = Solution()
t = s.uniquePaths(3,7)
print(t)