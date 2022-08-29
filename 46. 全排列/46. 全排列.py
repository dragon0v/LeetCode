class Solution:
    def permute(self, nums):
        def backtrack(idx,output):
            '''
            idx: 当前填的是第idx位数
            output: 当前排列
            '''
            
            