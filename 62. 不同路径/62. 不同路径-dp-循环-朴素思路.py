class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 数组循环方法
        matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    matrix[i][j] = 1
                elif i==0:
                    matrix[i][j] = matrix[i][j-1]
                elif j==0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-1]


s = Solution()
t = s.uniquePaths(3,7)
print(t)