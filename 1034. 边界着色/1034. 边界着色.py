from typing import *
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 思路是dfs一遍获取边界，再改边界颜色
        
        ori = grid[row][col]
        visited = [[0]*len(grid[0])]*len(grid)
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or visited[r][c] == 1:
                return
            visited[r][c] = 1
            if grid[r][c]==ori:
                if 
                dfs(r,c+1)
                dfs(r,c-1)
                dfs(r-1,c)
                dfs(r+1,c)
                
            else:
                return
        dfs(row,col)
        return grid

s = Solution()
t = s.colorBorder()
print(t)