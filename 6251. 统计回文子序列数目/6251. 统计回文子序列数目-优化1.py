from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import lru_cache


class Solution:
    def countPalindromes(self, s: str) -> int:
        # 核心思想还是暴力穷举，优化查找重复值
        # 超时，s长度200耗时14.4秒，快了正好1s
        if len(s)<5:
            return 0
        MOD = 10**9 + 7

        exist = defaultdict(list)  # 记录字符出现的位置
        for i,v in enumerate(s):
            exist[v].append(i)

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
                tl = exist[one]
                possible = tl[bisect_left(tl,i+1):bisect_right(tl,end)]
                for j in possible:
                    res += findsame(i+1,j-1,t+1) % MOD

                # for j in range(end,i+1,-1):  # 找重复值的过程可以优化
                #     if s[j]==one:
                #         # print(i,j,t)
                #         res += findsame(i+1,j-1,t+1) % MOD

            return res % MOD
        
        return findsame(0,len(s)-1,0)

s = Solution()
t = s.countPalindromes('0'*200)
# t = s.countPalindromes("0000000")
print(t)