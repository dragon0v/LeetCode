class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        # 每个元素有两个状态，选或不选
        def backtrack(crt,i):
            '''
            crt: 当前答案
            i: 当前增加的元素下标
            '''
            res.append(crt)
            for j in range(i,n):
                backtrack(crt+[nums[j]],j+1)

        backtrack([],0)
        return res

s = Solution()
t = s.subsets([1,2,3])
print(t)

# https://www.cnblogs.com/mozi-song/p/9579418.html#_label2_0
# ↑ 关于backtracking的合集教程

# 是抄题解的