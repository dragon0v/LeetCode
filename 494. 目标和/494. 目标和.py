class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        # 暴力法
        # 采用回溯法暴力枚举
        # 正确但是超时了
        self.ans = 0
        def backtrack(i,sum):
            if i==len(nums):
                if sum+nums[i-1]==target:
                    self.ans+=1
                if sum-nums[i-1]==target:
                    self.ans+=1
                return
            backtrack(i+1,sum+nums[i-1])
            backtrack(i+1,sum-nums[i-1])

        backtrack(1,0)
        return self.ans

s = Solution()
t = s.findTargetSumWays([1,1,1,1,1],3)
print(t)