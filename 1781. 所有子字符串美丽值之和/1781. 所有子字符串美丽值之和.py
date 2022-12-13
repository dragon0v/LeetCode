from typing import *
from collections import Counter, defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        # 子串考虑双指针
        # counter记录出现次数，minmax记录最大最小值对应的key,value
        # 写的一坨好shit
        n = len(s)
        res = 0
        for i in range(n):
            minmax = [[{s[i]},1],[s[i],1]]
            counter = defaultdict(int)
            counter[s[i]] = 1
            for j in range(i+1,n):
                k = s[j]
                v = counter[k]
                counter[k] = v+1
                if v+1 > minmax[1][1]:
                    minmax[1][1] = v+1
                    minmax[1][0] = k
                if minmax[0][0] == {k}:
                    minmax[0][1] += 1
                    # 这里需要更新全部值为v+1的key到minmax[0][0]
                    for kk,vv in counter.items():
                        if vv==v+1:
                            minmax[0][0].add(kk)
                elif k in minmax[0][0]:
                    minmax[0][0].remove(k)

                if v+1 < minmax[0][1]:
                    minmax[0][0] = {k}
                    minmax[0][1] = v+1
                    if v+1==minmax[1][1]:
                        minmax[0][0].add(minmax[1][0])
                elif v+1 == minmax[0][1]:
                    minmax[0][0].add(k)
                print(s[i:j+1],minmax)
                res += minmax[1][1] - minmax[0][1]
        return res

s = Solution()
t = s.beautySum("aabcb")
print(t)