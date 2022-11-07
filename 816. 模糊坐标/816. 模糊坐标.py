from typing import *
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def process(s):
            # 添加小数点
            if len(s)==1:
                return [s]
            res = [s]
            for i in range(1,len(s)):
                res.append('%s.%s'%(s[:i],s[i:]))
            
            return list(filter(lambda s:s[:2]!='00' and ('.' not in s or s[-1]!='0') and (s[0]!='0' or s[:2]=='0.'), res))
            

        s = s[1:-1]
        n = len(s)
        res = []
        for i in range(1,n):
            p1 = process(s[:i])
            p2 = process(s[i:])
            for a in p1:
                for b in p2:
                    res.append('(%s, %s)'%(a,b))
        
        return res

s = Solution()
# t = s.ambiguousCoordinates("(123)")
# t = s.ambiguousCoordinates("(0123)")
t = s.ambiguousCoordinates("(100)")
print(t)