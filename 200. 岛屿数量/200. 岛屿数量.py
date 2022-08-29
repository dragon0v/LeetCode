class Solution:
    def numIslands(self, grid):
        self.walked = [[0 for _ in range(len(grid[0]))] for p in range(len(grid))]
        print(self.walked)
        cnt = 0
        def dfs(i,j):
            if i<0 or i>=len(grid) or j < 0 or j>=len(grid[0]):
                return
            if self.walked[i][j] == 1:
                return
            if grid[i][j] == '0':
                return
            else:
                self.walked[i][j] = 1
                self.area += 1
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i,r in enumerate(self.walked):
            for j,c in enumerate(r):
                self.area = 0
                if c == 0:
                    dfs(i,j)
                    if self.area>0:
                        cnt += 1
        
        return cnt
                    

s = Solution()
t = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(t)

# ac，时间空间都垫底，有时间看看别人怎么写的