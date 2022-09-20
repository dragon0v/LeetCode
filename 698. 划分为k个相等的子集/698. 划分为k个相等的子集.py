from typing import *
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 思路：回溯；目标是把n个鸡蛋均分到k个篮子里
        # 使用dfs看是否能把第i个鸡蛋放到第j个篮子
        # 如果能看到第n个鸡蛋。就说明有这种放法
        # 参考 https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/by-lcbin-92ll/
        n = sum(nums)
        if n%k:
            return False
        part = n//k
        basket = [0] * k  # k个篮子
        nums.sort(reverse=True)  # 更快，减少搜索次数
        
        def dfs(i,basket):
            if i==len(nums):
                return True
            for j in range(k):
                # TODO 为什么这样剪枝能快这么多？？
                if j>0 and basket[j]==basket[j-1]:  # 剪枝，如果当前篮子和上一个篮子相同那么肯定是一样的结果
                    continue
                basket[j] += nums[i]
                if basket[j] <= part and dfs(i+1,basket):
                    return True
                basket[j] -= nums[i]  # 说明当前鸡蛋不能放在第j个篮子里
            print(i)
            return False  # 到这还没return True说明这个蛋四个篮子都不能放，无解

        return dfs(0,basket)



s = Solution()
# 无20行的剪枝，100s也没跑出来
t = s.canPartitionKSubsets([3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2],10)
print(t)