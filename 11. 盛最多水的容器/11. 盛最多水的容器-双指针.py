from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        # 双指针
        i = 0
        j = len(height)-1
        while i<j:
            if height[i] > height[j]:
                area = max(area, height[j]*(j-i))
                j -= 1
            else:
                area = max(area, height[i]*(j-i))
                i += 1
        return area

        

s = Solution()
t = s.maxArea([1,8,6,2,5,4,8,3,7])
print(t)