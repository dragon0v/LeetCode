from typing import *
'''
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre_product = 1
        back_product = 1
        for each in nums:
            res.append(pre_product)
            pre_product *= each
        for i in range(len(nums)-1,-1,-1):
            res[i] *= back_product
            back_product *= nums[i]
        return res
s = Solution().productExceptSelf([1,2,3,4,5])
print(s)