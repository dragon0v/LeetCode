class Solution:
    def findPeakElement(self, nums) -> int:
        # 必须是Ologn
        # 特殊情况输入为-2**31
        if len(nums) == 1:
            return 0

        # 你可以假设 nums[-1] = nums[n] = -∞
        nums = [-2**31] + nums + [-2**31]

        # 题目保证了相邻元素不相等，最简单的方法就是返回最大值的下标
        # 但是这个方法是O(n)的

        # 迭代爬坡法
        # 在中间随机找一个元素，每次向上走，指导两边都是下坡
        i = len(nums)//2
        while i >= 0 and i < len(nums):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i-1
            elif nums[i-1] > nums[i]:
                i -= 1
            else:
                i += 1
