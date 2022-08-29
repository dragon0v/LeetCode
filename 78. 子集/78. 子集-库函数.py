import itertools

class Solution:
    def subsets(self, nums):
        res = []
        for i in range(len(nums)+1):
            # 返回类型是元组
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


s = Solution()
t = s.subsets([1,2,3])
print(t)

# https://www.cnblogs.com/mozi-song/p/9579418.html#_label2_0
# ↑ 关于backtracking的合集教程

# 是抄题解的

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。