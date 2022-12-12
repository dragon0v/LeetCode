from typing import *
from collections import Counter, defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        # 子串考虑双指针
        # counter记录出现次数，minmax记录最大最小值对应的key,value

        n = len(s)
        res = 0
        for i in range(n):
            minmax = [[s[i],1],[s[i],1]]
            counter = defaultdict(int)
            counter[s[i]] = 1
            for j in range(i+1,n):
                k = s[j]
                v = counter[k]
                counter[k] = v+1
                if v+1>minmax[1][1]:
                    minmax[1][0] = k
                    minmax[1][1] = v+1
                if minmax[0][0] == k:  # 最大最小值是同一个字符
                    minmax[0][1] = v+1
                if v+1<minmax[0][1]:
                    minmax[0][0]=k
                    minmax[0][1]=v+1
                res += minmax[1][1]-minmax[0][1]
                print(minmax)
            
        return res

s = Solution()
t = s.beautySum("aabcb")
print(t)