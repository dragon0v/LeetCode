class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = left_max = nums[0]
        left_pos = 0
        for i in range(1, n - 1):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max, left_pos = cur_max, i
        return left_pos + 1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/partition-array-into-disjoint-intervals/solutions/1913934/fen-ge-shu-zu-by-leetcode-solution-t4pm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。