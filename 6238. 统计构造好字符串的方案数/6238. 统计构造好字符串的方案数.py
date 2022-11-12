from typing import *
from functools import lru_cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 一眼DP，不加 @ cache是超时的，加了内存消耗上百兆，但时间很快
        # @ cache需要py39，低版本可以用 @ lru_cache(maxsize=None)，@cache性能会更好，因为无需移出旧值
        MOD = 10**9+7
        # dp，长度为dp[s] = dp[s-zero] + dp[s-one]
        if zero%one==0 or one%zero==0:
            ishz = True
        else:
            ishz = False
        # @ cache
        @ lru_cache(maxsize=None)
        def dfs(s,ishz,zero,one):
            # 互质需做区分
            if s<=0:
                return 0
            if ishz:
                if s==max(zero,one):  # 相同也是2
                    return 2
                if s==min(zero,one):
                    return 1
                
            else:
                if s==zero or s==one:
                    return 1
            
            return (dfs(s-zero,ishz,zero,one)+dfs(s-one,ishz,zero,one)) % MOD
        
        return sum(dfs(i,ishz,zero,one) for i in range(low,high+1)) % MOD


s = Solution()
t = s.countGoodStrings(1,9999,2,3)
print(t)