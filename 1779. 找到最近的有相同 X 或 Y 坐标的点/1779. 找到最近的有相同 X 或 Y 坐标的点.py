class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        m = 10**9
        for i,(a,b) in enumerate(points):
            t = (abs(a-x)+abs(b-y))
            if (a==x or b==y) and t<m:
                res = i
                m = t
        
        return res