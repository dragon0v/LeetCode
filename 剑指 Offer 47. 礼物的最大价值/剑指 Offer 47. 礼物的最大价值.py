class Solution:
    def maxValue(self, grid) -> int:
        # 第i行j列的最大值仅由i-1行j列和i-1行j-1列的值决定
        # m[i][j] = v[i][j] + max(m[i-1][j],m[i-1][j-1]+v[i][j-1]) (i!=0)
        # m[0][j] = v[0][j] + v[0][j-1] (j!=0)
        
        # 不对，不是只能走一格，可以一直走下去
        
        mi = [grid[0][0]]+[(grid[0][j-1]+grid[0][j]) for j in range(1,len(grid[0]))]
        print(0,mi)
        for i in range(1,len(grid)):
            for j in range(len(grid[0])-1,0,-1):
                mi[j] = max(mi[j-1]+grid[i][j-1],mi[j]) + grid[i][j]
            mi[0] += grid[i][0]
        
        return max(mi)
                
        

s = Solution().maxValue([[1,2,3],[2,3,4]])
print(s)