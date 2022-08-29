from typing import *
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 对于每个房屋，找它在左右最近的供暖期
        ch = 0 # 当前供暖期的下标
        r = 0 # 最大半径，返回值
        cr = r # 当前半径
        n = len(heaters)
        houses.sort()
        heaters.sort()
        for house in houses:
            # print(cr,r)
            while ch+1 < n and house > heaters[ch+1]:
                ch += 1
            if ch+1 < n:
                # assert heaters[ch] <= house <= heaters[ch+1]
                cr = min(abs(house-heaters[ch]),abs(house-heaters[ch+1]))
            else:
                cr = abs(house-heaters[ch])
            r = max(cr,r)
        
        return r

s = Solution()
t = s.findRadius([10002, 14000, 28000, 45780, 45877, 47021, 62265, 98494],
                [1653, 7424, 11480, 11543, 13752, 14354, 44128, 78448, 82337, 82356])
print(t)