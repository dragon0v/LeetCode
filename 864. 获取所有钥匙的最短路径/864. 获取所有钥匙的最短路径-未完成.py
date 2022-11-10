from typing import *
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # 错
        numkey = 0
        r,c = len(grid), len(grid[0])
        visited = [[14 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                cc = grid[i][j]
                if cc in 'abcdef':
                    numkey+=1
                if cc=='@':
                    start = (i,j)
                    grid[i] = grid[i].replace('@','.')
        ownedkey = set()
        l = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f', '#':'xx'}
        self.res = 2000
        def dfs(i,j,steps=0):
            visited[i][j] -= 1
            cc = grid[i][j]
            if cc in 'abcdef':
                ownedkey.add(cc)
                if len(ownedkey)==numkey:
                    self.res = min(self.res,steps)
                    return self.res
            
            if i+1<r and visited[i+1][j]>=0 and grid[i][j]!='#' and any([grid[i+1][j] not in 'ABCDEF', l[grid[i+1][j]] in ownedkey]):
                dfs(i+1,j,steps+1)
            if i+1>=0 and visited[i-1][j]>=0 and grid[i][j]!='#' and any([grid[i-1][j] not in 'ABCDEF', l[grid[i-1][j]] in ownedkey]):
                dfs(i-1,j,steps+1)
            if j+1<c and visited[i][j+1]>=0 and grid[i][j]!='#' and any([grid[i][j+1] not in 'ABCDEF', l[grid[i][j+1]] in ownedkey]):
                dfs(i,j+1,steps+1)
            if j-1>=0 and visited[i][j-1]>=0 and grid[i][j]!='#' and any([grid[i][j-1] not in 'ABCDEF', l[grid[i][j-1]] in ownedkey]):
                dfs(i,j-1,steps+1)
            print(steps,self.res)
            return self.res
        
        return dfs(start[0],start[1],0)


s = Solution()
t = s.shortestPathAllKeys(["@.a.#","###.#","b.A.B"])
print(t)