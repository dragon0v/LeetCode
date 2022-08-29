class Solution:
    def getBiggestThree(self, grid):
        # 以第i,j为上顶点的a*a菱形必须满足
        # i-a+1>=0 i+a+1<=m-1 j+2*a-1 <= n
        a = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                for k in range(1,2+min((n-1)//2,(m-1)//2)):
                    if j-k+1 < 0 or j+k-1 > n-1 or i+2*k-2 > m-1:
                        break
                    tempsum = 0
                    # print(i,j,k)
                    for t in range(k):
                        if t==0:
                            if i==i+2*k-2:
                                tempsum = tempsum + grid[i][j]
                            else:
                                tempsum = tempsum + grid[i][j] + grid[i+2*k-2][j]
                        elif t==k-1:
                            tempsum = tempsum + grid[i+t][j+t] + grid[i+t][j-t]
                        else:
                            tempsum = tempsum + grid[i+t][j+t] + grid[i+t][j-t] + grid[i+2*k-2-t][j+t] + grid[i+2*k-2-t][j-t]
                    a.append(tempsum)
                    
        
        a=list(set(a))
        a.sort(reverse = True)
        if len(a)>=3:
            return a[:3]
        return a