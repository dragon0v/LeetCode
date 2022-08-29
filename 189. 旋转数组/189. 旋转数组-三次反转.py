class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

# 作者：RUMIF
# 链接：https://leetcode-cn.com/problems/rotate-array/solution/pythonku-han-shu-fan-zhuan-lie-biao-by-r-1rju/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？ 
# 只有三次反转满足这个条件