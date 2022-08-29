from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        num1 = num2 = None # 当前选出的前两个数
        cnt1 = cnt2 = 0 # 当前两数的计数
        
        for num in nums:
            # if的顺序有影响，例如输入[2,2]，先判断cnt2==0就会导致res=[2,2]
            # 还是有问题，[4,1,2,3,4,4,3,2,1,4]会返回[4,4]
            if cnt1 > 0 and num == num1:
                cnt1 += 1
            elif cnt2 > 0 and num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 += 1
            elif cnt2 == 0:
                num2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        # 此时待选的答案必在num1，num2中
        n = len(nums)
        # 这里和官方解比，循环多了一次，但是少了两个中间变量
        for candidate in set([num1,num2]):
            if sum([num==candidate for num in nums]) > n//3:
                res.append(candidate)
        
        return res
                
        
        

# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
# 摩尔投票的推广
# 摩尔投票法的核心是抵消，对于多于n/2的众数，众数最多只有一个，
# 每次取两个不同的数抵消，最后剩下来的就是众数
# 推广到多于n/3的众数，复合条件的众数最多2个，
# 每次取3个不同的数抵消，生下来的就是众数

s = Solution().majorityElement([33,33])
print(s)