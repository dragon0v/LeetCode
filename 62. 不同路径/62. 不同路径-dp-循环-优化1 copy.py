class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 数组循环方法
        # 优化1：matrix第一行第一列一定是1，顺序递推，省去了边界判断
        # 进一步优化matrix的初始化
        matrix = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]


s = Solution()
t = s.uniquePaths(3,7)
print(t)