from typing import *
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 两次遍历
        n = len(boxes)
        left = [0 for i in range(n+1)]  # 储存下标i左边的球移动到i的cost
        right = [0 for i in range(n+1)]
        l = r = 0  # 当前左右侧积累的球数

        for i,v in enumerate(boxes):
            left[i+1] = left[i] + l
            if v=='1':
                l += 1
        for i,v in enumerate(boxes[::-1]):
            right[n-1-i] = right[n-i] + r
            if v=='1':
                r += 1
        
        left.pop(0)
        right.pop()
        return [l+r for l,r in zip(left,right)]  # 也可以在更新left和right的同时更新答案数组

s = Solution()
t = s.minOperations("001011")
print(t)
