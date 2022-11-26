class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # 直接根据题意编程即可
        m = len(grid[0])
        n = len(grid)
        d = [[],[],[],[]]
        for i in range(n):
            t = sum(grid[i])
            d[0].append(t)
            d[2].append(m-t)
        for j in range(m):
            t = sum([grid[i][j] for i in range(n)])
            d[1].append(t)
            d[3].append(n-t)
        
        print(d)
        for i in range(n):
            for j in range(m):
                grid[i][j] = d[0][i] + d[1][j] - d[2][i] - d[3][j]
        
        return grid