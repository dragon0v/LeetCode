from functools import lru_cache


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 第i行第j个杯子满了之后会流到[i+1,j] [i+1,j+1]
        # dp[i][j] = max(0,(dp[i-1][j]-1))/2 + max(0,(dp[i-1][j-1]-1))/2
        # 递归式dp，费内存
        @ lru_cache(None)  # 不加cache超时，因为虽然i是递减的，j是有可能重复计算的
        def dfs(i,j):
            if j<0 or j>i:
                return 0
            if i==0:
                return poured
            else:
                # print(i,j,max(0,(dfs(i-1,j)-1))/2 + max(0,(dfs(i-1,j-1)-1))/2)
                return max(0,(dfs(i-1,j)-1))/2 + max(0,(dfs(i-1,j-1)-1))/2
        
        return min(1,dfs(query_row,query_glass))

s = Solution()
# t = s.champagneTower(2,1,1)
# print(t)
t = s.champagneTower(25,6,1)
print(t)