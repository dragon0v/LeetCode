from typing import *
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        # 要求时间n，空间1
        
        # 参考 https://leetcode.cn/problems/missing-two-lcci/solution/zhuan-zhi-xiao-shi-de-shu-de-san-chong-jie-fa-by-w/
        # 思路：求和，如果只缺少一个数那很简单求和相减即可
        # 缺少两个的话，将数分成两组即可
        n = len(nums)+2
        sum2 = n * (n + 1) // 2 - sum(nums)  # 两个数的和
        limit = sum2//2  # 一个数必小于对于limit，一个数必大于limit
        sum1=0
        for x in nums:
            if x<=limit:
                sum1 += x
        
        a = limit * (limit + 1) // 2 - sum1
        return [a,sum2-a]

s = Solution()
t = s.missingTwo([1])
print(t)