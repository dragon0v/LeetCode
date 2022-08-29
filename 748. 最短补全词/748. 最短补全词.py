from typing import *
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dl = dict()
        res = []
        # 仅counter字符
        for c in licensePlate:
            if ord(c)>=ord('a') and ord(c)<=ord('z'):
                if c in dl.keys():
                    dl[c] += 1
                else:
                    dl[c] = 1
            elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
                k = chr(ord(c)-ord('A')+ord('a'))
                if k in dl.keys():
                    dl[k] += 1
                else:
                    dl[k] = 1
        
        for word in words:
            dd = dl.copy()
            flag = True
            unused = 0
            for c in word:
                if c in dd.keys():
                    dd[c] -= 1
                    if dd[c] < 0:
                        unused += 1
                else:
                    unused += 1
            for t in dd.values():
                if t>0:
                    flag = False
            if flag:
                res.append((word,unused))
                
        res.sort(key=lambda x:x[1])
        return res[0][0]


licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
s = Solution().shortestCompletingWord(licensePlate,words)
print(s)