from typing import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 思路：重新排序，摆烂做法，因为没有用到题中已排序的条件
        arr.sort(key=lambda a:abs(a-x))
        return sorted(arr[:k])

s = Solution()
t = s.findClosestElements([1,2,3,4,5,6],1,3)
print(t)