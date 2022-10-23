class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        # 不优雅
        res = ''
        t = len(w2)
        for i in range(len(w1)):
            res += w1[i]
            if i<t:
                res += w2[i]
        if t>len(w1):
            res += w2[len(w1):]
        return res