from typing import *
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # 简单模拟
        c = Counter()
        for rec in cpdomains:
            rep, domain = rec.split(' ')
            ds = domain.split('.')
            t = len(ds)
            for d in range(t):
                c['.'.join(ds)] += int(rep)
                ds.pop(0)
        
        res = []
        for k,v in c.items():
            res.append(str(v)+" "+k)
        return res
        # 更优雅的方式
        return [f"{v} {k}" for k,v in c.items()]
