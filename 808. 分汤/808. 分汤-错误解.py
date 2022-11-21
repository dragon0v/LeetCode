from collections import Counter
from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        # 思路对，但错误解，res=aaaazaazbazbb 13位,实际上应该是aaaaaaazaazbazbb 16位
        @lru_cache(None)
        def dfs(a,b):
            if a<=0 and b>0:
                return 'a'
            if a<=0 and b<=0:
                return 'z'
            if a>0 and b<=0:
                return 'b'
            print(dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))
            return dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75)
        
        res = dfs(n,n)
        c = Counter(res)
        print(res,len(res))
        return (c['a'] + c['z']/2) / len(res)
            
s = Solution()
t = s.soupServings(100)
print(t)