from typing import *
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates = [0 for _ in range(len(s))]
        t = 0
        for i,c in enumerate(s):
            if c=='|':
                if t>0:
                    plates[i] = t
                    t = 0
                else:
                    plates[i] = 0.0000000001
            else:
                t += 1
        print(plates,len(s))
        res = []
        for q in queries:
            r = 0
            cnt = 0
            for v in plates[q[0]:q[1]+1]:
                if v!=0:
                    cnt += 1
                    if cnt > 1 and v>0.5:
                        r += v//1
            res.append(r)
        return res
# 超时

s = Solution().platesBetweenCandles('**|**|***|',[[2,5],[5,9]])
print(s)