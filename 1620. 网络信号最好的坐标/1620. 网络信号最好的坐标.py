from typing import *
from math import sqrt, floor


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # 纯暴力，三重循环
        # 官解居然也是暴力枚举，只是做了预处理xy坐标最大值的操作
        def calsig(x,y,q,a,b):
            dist = sqrt((a-x)**2+(b-y)**2)
            if dist>radius:
                return 0
            return floor(q/(1+dist))
        
        maxsig = 0
        res = []
        for a in range(51):
            for b in range(51):
                t = 0
                for x,y,q in towers:
                    t += calsig(x,y,q,a,b)
                if t==maxsig:  # 优化：由于ab是按顺序枚举的，所以直接在t>maxsig保存res，无需=的判断
                    res.append([a,b])
                if t>maxsig:
                    res = [[a,b]]
                    maxsig = t
                t = 0
                    
        return sorted(res)[0]

# 2300ms, 击败42%

s = Solution()
t = s.bestCoordinate([[1,2,5],[2,1,7],[3,1,9]],2)
print(t)