from typing import *
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈，倒序遍历nums2
        d = dict()
        stack = []  # 栈顶记录右边最大的数，栈顶至栈底递增
        for n in nums2[::-1]:
            # 从后往前看，最后得到的stack栈顶元素就是n的下一个更大元素
            while stack and n>=stack[-1]:
                stack.pop()
            d[n] = stack[-1] if stack else -1
            stack.append(n)
        
        return [d[x] for x in nums1]

s = Solution()
t = s.nextGreaterElement([4,1,2],[1,3,4,2])
print(t)