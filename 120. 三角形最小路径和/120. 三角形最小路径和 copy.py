from typing import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[3][2] = t[3][2] + min(dp[2][1],dp[2][2])
        dp = [10**4+3 for _ in range(len(triangle)+1)]
        dp[0]=triangle[0][0]
        if len(triangle)==1:
            return triangle[0][0]
        for t in triangle[1:]:
            tdp = dp[::]
            for i,each in enumerate(t):
                if i == 0:
                    dp[i] = each + tdp[i]
                else:
                    dp[i] = each + min(tdp[i-1],tdp[i])

        print(dp)
        return min(dp)

# 优化是使用线性额外空间，把dp改成长度为最下层数量即可
s = Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(s)