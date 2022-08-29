class Solution:
    def findDuplicate(self, nums):
        occurred = [False for i in range(len(nums)+1)]
        for each in nums:
            if occurred[each]:
                return each
            else:
                occurred[each] = True

# 由于题目给的n在3*10^4，可以用这种方法，牺牲内存换时间
# 时间是很好的

# 未修改nums，时间复杂度小于n2
# 接下来尝试不使用额外空间