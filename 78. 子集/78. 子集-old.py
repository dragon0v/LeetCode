# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:42:31 2021

@author: ToxicNeoBanana
"""

#78. 子集

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        #对于每个元素只有两种情况，选它或不选它
        def backtrack(nums,current,index,res):
            
        
        backtrack(nums,[],0,res)
        return res