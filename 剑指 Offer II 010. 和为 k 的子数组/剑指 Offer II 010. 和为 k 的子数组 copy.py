class Solution:
    def subarraySum(self, nums, k):
        ret = pre_sum = 0
        pre_dict = {0: 1}
        for i in nums:
            pre_sum += i
            ret += pre_dict.get(pre_sum - k, 0)
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
        return ret

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/QTMn0o/solution/shua-chuan-jian-zhi-offer-day07-shu-zu-i-jdnu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。