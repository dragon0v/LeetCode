from typing import *
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # 需要2T多内存，纯粹牛马解答
        visited = [[False for _ in range(10**3)] for _ in range(10**3)]
        x = y = 0
        for i,v in enumerate(distance):
            direction = i % 4
            for j in range(v):
                if visited[x][y] == True:
                    return False
                else:
                    visited[x][y] = False
                # 0向上，y+=v
                # 1向左，x-=v
                # 2向下，y-=v
                # 3向右，x+=v
                if direction==0:
                    y += v
                elif direction == 1:
                    x -= v
                elif direction == 2:
                    y -= v
                else:
                    x += v
        return True
                

s = Solution()
t = s.isSelfCrossing([1,2,3,4])
print(t)