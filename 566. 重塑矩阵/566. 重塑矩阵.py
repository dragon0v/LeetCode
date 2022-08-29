class Solution:
    def matrixReshape(self, nums, r, c):
        d = len(nums)*len(nums[0])
        if(r*c != d):
            return nums
        ori = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                ori.append(nums[i][j])
        res = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = ori.pop(0)
        return res

# 时间空间都不理想
# 考虑每次读一个并写入结果