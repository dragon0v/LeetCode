class Solution:
    def reformat(self, s: str) -> str:
        n = []
        c = []
        for i in s:
            if i.isnumeric():
                n.append(i)
            else:
                c.append(i)
        
        if abs(len(n)-len(c)) > 1:
            return ""
        res = ''
        if len(n)>len(c):
            t = [n,c]
        else:
            t = [c,n]
        for i in range(len(n)+len(c)):
            res += t[i%2][i//2]
        return res
# 太不优雅了，双O(n)