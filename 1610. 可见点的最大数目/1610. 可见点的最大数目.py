from typing import *
from math import atan2, pi
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        points = [[point[0]-location[0],point[1]-location[1]] for point in points]
        print(points)
        # 站在点上的情况
        res = 0
        for i,v in enumerate(points):
            if v==[0,0]:
                points.pop(i)
                res += 1
        angles = [atan2(point[1],point[0])*180/pi for point in points]
        print(angles)
        angles.sort()
        print(angles)
        n = len(angles)
        i,j = 0,0
        m = cm = 0
        while j<n:
            if angles[j] - angles[i] <= angle:
                j += 1
                cm += 1
            else:
                i += 1
                m = max(m,cm)
                cm -= 1
        m = max(m,cm)

        # 135,-135 相差90度
        for i,v in enumerate(angles):
            if v<=0:
                angles[i] = 360+v
        i,j = 0,0
        cm = 0
        angles.sort()
        while j<n:
            if angles[j] - angles[i] <= angle:
                j += 1
                cm += 1
            else:
                i += 1
                m = max(m,cm)
                cm -= 1
        m = max(m,cm)


        return m + res


s = Solution()
t = s.visiblePoints([[2,1],[2,2],[3,3],[-1,-1],[2,-3],[8,-7]],90,[1,1])
print(t)