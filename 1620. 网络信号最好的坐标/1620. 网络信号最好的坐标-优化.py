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
        
        # 预处理坐标最大值
        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        maxsig = 0
        res = [0,0]  # 需要有初值，信号都为0的时候，对应初值[0,0]，没优化版恰巧无意识地避开了这点
        for a in range(x_max+1):
            for b in range(y_max+1):
                t = 0
                for x,y,q in towers:
                    t += calsig(x,y,q,a,b)
                # 优化：由于ab是按顺序枚举的，所以直接在t>maxsig保存res，无需=的判断
                if t>maxsig:
                    res = [a,b]
                    maxsig = t
                t = 0
                    
        return res

# 2088ms, 击败60%

s = Solution()
t = s.bestCoordinate([[1,2,5],[2,1,7],[3,1,9]],2)
print(t)