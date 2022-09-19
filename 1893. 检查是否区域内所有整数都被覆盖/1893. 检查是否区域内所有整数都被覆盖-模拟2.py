from typing import *
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            covered = False
            for l,r in ranges:
                if l<=i<=r:
                    covered = True
                    break
            if not covered:
                return False
        
        return True


# 模拟，其实不需要space数组，因为只有一个left&right，直接看就行了