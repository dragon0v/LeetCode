class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        w = len(grid[0])
        h = len(grid)
        visited = [[0 for _ in range(w)] for _ in range(h)]
        # print(visited)
        islands = []
        def area(x,y,tarea,visited):
            # 当前是岛屿，要计算面积
            if grid[x][y] == 1:
                tarea += 1
                if x-1 >= 0 and grid[x-1][y]==1:
                    
            # 当前是海，要找岛屿
            else:
                
        

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution().maxAreaOfIsland(grid)
print(s)