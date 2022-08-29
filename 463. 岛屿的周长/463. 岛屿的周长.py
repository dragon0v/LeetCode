class Solution:
    def islandPerimeter(self, grid) -> int:
        m = len(grid[0])
        n = len(grid)
        visited = [[0 for i in range(m)] for _ in range(n)]
        res = 0

        #print(visited)
        def dfs(i,j):
            if i>=n or i<0 or j>=m or j<0:
                return
            visited[i][j] = 1
            # is an island, calculate perimeter
            if grid[i][j] == 1:
                pass

        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 1:
                    dfs(ii,jj)
        
        return res