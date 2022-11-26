from functools import lru_cache


class Solution:
    def countPalindromes(self, s: str) -> int:
        # 核心思想还是暴力穷举
        # 超时，s长度200耗时15.4秒
        if len(s)<5:
            return 0
        MOD = 10**9 + 7
        @lru_cache(None)
        def findsame(sta,end,t=0):
            # print(sta,end,t,11111)
            # 找s和e之间
            if t==2:
                return end-sta+1
            if end<sta:
                return 0
            res = 0
            for i in range(sta,end+1):
                one = s[i]
                for j in range(end,i+1,-1):  # 找重复值的过程可以优化
                    if s[j]==one:
                        # print(i,j,t)
                        res += findsame(i+1,j-1,t+1) % MOD
            return res % MOD
        
        return findsame(0,len(s)-1,0)

s = Solution()
t = s.countPalindromes('0'*200)
print(t)