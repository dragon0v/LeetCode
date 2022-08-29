class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        # DP计数
        ans = 0
        t = 1 # t控制子数组个数，连续的n个等差数字的全部等差子数组为1+2+3+...+(n-2)个
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                ans += t
                t += 1
            else:
                t = 1
        return ans