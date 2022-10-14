from typing import *
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # # 首先不考虑重复，一个新char的加入为所有已有组合的带来一个新的组合，同时还有他自己：
        # # dp[i] = sum(dp)+1
        # # 考虑重复，上面重复的情况是当且仅当有相同字符在组合最后，合计dpc[c]个
        # dp = [0 for _ in range(26)]
        # dpc = [-1 for _ in range(26)]
        # MOD = 10**9+7
        # for i,c in enumerate(s):
        #     dp[i] = (sum(dp) + 1)
        #     dpc[ord(c)-ord('a')] += 1
        #     dp[i] -= dpc[ord(c)-ord('a')]
        
        # return sum(dp) % MOD
        pass

# 错误的解
s = Solution()
t = s.distinctSubseqII('lee')
print(t)