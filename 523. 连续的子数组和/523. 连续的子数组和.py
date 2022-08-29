from itertools import accumulate

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        # 前缀和，连续子数组的和等于前缀和的差
        # 当两个前缀和相减能被k整除时，满足这两个前缀和除k的余数相同
        if len(nums)<2:
            return False
        
        preSum = list(accumulate(nums))
        occured = [-1 for _ in range(k+1)]# 不确定要不要+1，加了保险
        print(preSum)
        for i,each in enumerate(preSum):
            print(occured)
            r = each%k
            if occured[r] != -1:
                if i-occured[r]>=2:
                    return True
            else:
                occured[r] = i
        return False
        
s = Solution().checkSubarraySum([23,2,4,6,6],7)
print(s)