from typing import *
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 从边界开始跑两个dfs，看那个格子能否流到两个洋
        m,n = len(heights), len(heights[0])
        self.canPO = [[False for _ in range(n)] for _ in range(m)]
        self.canAO = [[False for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        # print(heights)
        # print(self.canAO)

        def dfs(r,c):
            if visited[r][c]:
                return self.canPO[r][c],self.canAO[r][c]
            visited[r][c] = True
            border = False
            if r==0:
                self.canPO[r][c] = True
                border = True
            if r==m-1:
                self.canAO[r][c] = True
                border = True
            if c==0:
                self.canPO[r][c] = True
                border = True
            if c==n-1:
                self.canAO[r][c] = True
                border = True
            if border:
                return self.canPO[r][c], self.canAO[r][c]
            
            if r-1>=0 and heights[r][c] <= heights[r-1][c]:
                self.canPO[r][c] |= dfs(r-1,c)[0]
                self.canAO[r][c] |= dfs(r-1,c)[1]
            if r+1<m and heights[r][c] <= heights[r+1][c]:
                self.canPO[r][c] |= dfs(r+1,c)[0]
                self.canAO[r][c] |= dfs(r+1,c)[1]
            if c-1>=0 and heights[r][c] <= heights[r][c-1]:
                self.canPO[r][c] |= dfs(r,c-1)[0]
                self.canAO[r][c] |= dfs(r,c-1)[1]
            if c+1<n and heights[r][c] <= heights[r][c+1]:
                self.canPO[r][c] |= dfs(r,c+1)[0]
                self.canAO[r][c] |= dfs(r,c+1)[1]

            return self.canPO[r][c], self.canAO[r][c]
            
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        
        res = []
        for i in range(m):
            for j in range(n):
                if self.canAO[i][j] and self.canPO[i][j]:
                    res.append([i,j])
        
        print(self.canPO)
        print(self.canAO)
        return res

s = Solution()
t = s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(t)