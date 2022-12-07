class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 动态规划，dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # 数组循环方法
        m,n = len(obstacleGrid[0]), len(obstacleGrid)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i==0 and j==0:
                    obstacleGrid[i][j] = 1
                elif i==0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j==0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
