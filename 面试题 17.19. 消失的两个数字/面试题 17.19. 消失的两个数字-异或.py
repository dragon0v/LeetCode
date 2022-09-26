from typing import *
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        # 要求时间n，空间1
        
        # 参考 https://leetcode.cn/problems/missing-two-lcci/solution/zhuan-zhi-xiao-shi-de-shu-de-san-chong-jie-fa-by-w/
        # 思路：位运算异或，如果只缺少一个数那很简单异或相减即可
        # 缺少两个的话，将数分成两组即可
        n = len(nums)+2
        xor2 = 0  # 两个数的异或值
        for i in range(1,n+1):
            xor2 ^= i
        for x in nums:
            xor2 ^= x
        
        a = 0  # 其中的一个数
        # TODO diff是啥，其中的数学原理可以学一学（xor的性质）
        diff = xor2 & -xor2
        for i in range(1,n+1):
            if diff&i:
                a ^= i
        for x in nums:
            if diff&x:
                a ^= x
        
        return [a, xor2^a]

s = Solution()
t = s.missingTwo([1])
print(t)