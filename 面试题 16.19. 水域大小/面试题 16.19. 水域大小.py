class Solution:
    def pondSizes(self, land):
        
        def dfs(i,j):
            print(i,j,self.visited)
            if(i<0 or i>=self.m or j<0 or j>=self.n or self.visited[i][j]==1):
                return

            self.visited[i][j] = 1
            if(land[i][j] == 0):
                self.area+=1
                print("OK",i,j,self.area)
                dfs(i-1,j-1)
                dfs(i-1,j)
                dfs(i-1,j+1)
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i+1,j-1)
                dfs(i+1,j)
                dfs(i+1,j+1)
            return

        self.m=len(land)
        self.n=len(land[0])
        self.visited = [[0] * self.n] * self.m
        print(self.m,self.n)
        # print(self.visited)
        res=[]
        # self.area=0
        for ii in range(self.m):
            for jj in range(self.n):
                self.area = 0
                dfs(ii,jj)
                if self.area > 0:
                    res.append(self.area)

        return res

s = Solution()
print(s.pondSizes([[1,2,1],[0,0,0]]))