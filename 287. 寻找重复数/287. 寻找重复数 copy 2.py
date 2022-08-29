class Solution:
    def findDuplicate(self, nums):
        for i,n in enumerate(nums):
            if n>len(nums):
                nums.append(n)
            elif nums[n+1] == n:
                return n
            else:
                nums[i],nums[n+1] = nums[n+1],nums[i]

# 尝试不使用额外空间,shibai?

