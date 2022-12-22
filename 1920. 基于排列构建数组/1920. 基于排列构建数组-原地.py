class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 进阶：原地修改
        # 思路：nums在0-999之间，可以将nums的低3位用来表示原数字，高3位表示新数字
        n = len(nums)
        # 第一次遍历编码最终值
        for i in range(n):
            low = nums[nums[i]] % 1000  # 低位表示原数字
            nums[i] += 1000 * low  # 高位表示新数字
        # 第二次遍历修改为最终值
        for i in range(n):
            nums[i] //= 1000
        return nums

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/build-array-from-permutation/solutions/858017/ji-yu-pai-lie-gou-jian-shu-zu-by-leetcod-gjcn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。