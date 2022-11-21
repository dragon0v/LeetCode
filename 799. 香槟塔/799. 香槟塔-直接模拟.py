class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 第i行第j个杯子满了之后会流到[i+1,j] [i+1,j+1]
        # dp[i][j] = max(0,(dp[i-1][j]-1))/2 + max(0,(dp[i-1][j-1]-1))/2
        # 直接模拟，速度比dp慢1/2
        glasses = [[0] * (query_row+2) for _ in range(query_row+2)]
        glasses[0][0] = poured
        for i in range(1,query_row+1):
            for j in range(i+1):
                if j>=0:
                    glasses[i][j] = max(0,glasses[i-1][j]-1)/2 + max(0,glasses[i-1][j-1]-1)/2
                else:
                    glasses[i][j] = max(0,glasses[i-1][j]-1)/2
        
        return min(glasses[query_row][query_glass],1)




s = Solution()
t = s.champagneTower(2,1,1)
print(t)
t = s.champagneTower(25,6,1)
print(t)
t = s.champagneTower(900000009,99,88)
print(t)