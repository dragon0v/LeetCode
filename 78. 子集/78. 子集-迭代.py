import itertools

class Solution:
    def subsets(self, nums):
        res = [[]] # res初始值为[[]]，也就是第一个元素为[]
        for newnum in nums:
            # 每个后面的元素加上res中已有的每一个，res元素每次增加1,2,4,8...个
            # 非常精妙！！！
            # res中元素的顺序是倒序，把[newnum]和oldnum for... 调换顺序会报错，
            # 只能list+generator，不能反过来
            res = res + [[newnum] + oldnum for oldnum in res]
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