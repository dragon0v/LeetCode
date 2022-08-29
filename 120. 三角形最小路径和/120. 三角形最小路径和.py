from typing import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[3][2] = t[3][2] + min(dp[2][1],dp[2][2])
        dp = []
        dp.append(triangle[0])
        if len(triangle)==1:
            return triangle[0][0]
        for t in triangle[1:]:
            tdp = []
            for i,each in enumerate(t):
                if i == 0:
                    tdp.append(each + dp[-1][i])
                elif i == len(t)-1:
                    tdp.append(each + dp[-1][i-1])
                else:
                    tdp.append(each + min(dp[-1][i-1],dp[-1][i]))
            dp.append(tdp)
            





        return min(dp[-1])

# 优化是使用线性额外空间，把dp改成长度为最下层数量即可
s = Solution()
print(s)