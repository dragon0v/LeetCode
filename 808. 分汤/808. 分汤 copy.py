from collections import Counter
from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        # 超时后发现当n大于一定值后答案永远是1
        if n>10000:
            return 1.0
        @lru_cache(None)
        def dfs(a,b):
            if a<=0 and b>0:
                return 1
            if a<=0 and b<=0:
                return 0.5
            if a>0 and b<=0:
                return 0
            return (dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75)) / 4
        
        return dfs(n,n)
            
s = Solution()
t = s.soupServings(100)
print(t)