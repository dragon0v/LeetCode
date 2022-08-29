# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:08:03 2019

@author: NeoBanana
"""

#https://leetcode-cn.com/problems/single-number-iii/

'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
'''

class Solution:
    def singleNumber(self, nums):
        exist=[]
        for i in range(len(nums)):
            if nums[i] in exist:
                exist.remove(nums[i])
            else:
                exist.append(nums[i])
        print(exist)
        return exist
#1350ms, 15.5MB
        
class Solution2:#仅把list变为set就省了很多时间
    def singleNumber(self, nums):
        exist=set()
        for i in range(len(nums)):
            if nums[i] in exist:
                exist.remove(nums[i])
            else:
                exist.add(nums[i])
        print(exist)
        return exist
#90ms, 15.8MB

#TODO 位运算？
Solution().singleNumber([1,2,3,4,5,3,2,1])














