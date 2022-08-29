class Solution:
    def numIslands(self, grid):
        def dfs(i,j):
            if i<0 or i>=len(grid) or j < 0 or j>=len(grid[0]):
                return
            if grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i,j)
        
        return cnt

s = Solution()
t = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","1"]])
print(t)

# ac，时间空间都还可以了

# 可以在原数组上操作，走过就把grid[i][j]置为'0'
# 主循环遍历整个矩阵，遇到'1'就执行dfs，并吧cnt+1