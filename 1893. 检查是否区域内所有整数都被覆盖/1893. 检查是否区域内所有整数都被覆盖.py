from typing import *
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        space = [0 for _ in range(55)]
        for r in ranges:
            for i in range(r[1]-r[0]+1):
                space[i+r[0]] = 1
        
        print(space)
        return all([space[i] for i in range(left,right+1)])

# 最基础的模拟