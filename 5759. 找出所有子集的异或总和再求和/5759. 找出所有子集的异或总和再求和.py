class Solution:
    def subsetXORSum(self, nums) -> int:
        # 求全部子集的方法
        subsets = [[]] # 空集必定是子集
        for i in range(len(nums)):
            for j in range(len(subsets)): # 在空集的基础上增加元素
                subsets.append(subsets[j]+[nums[i]])
        print(subsets)
        
        def XOR(li):
            r = 0
            for each in li:
                r^=each
            return r
        
        res = 0
        for each in subsets:
            res += XOR(each)
        return res