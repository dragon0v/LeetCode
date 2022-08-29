# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗?
# 你可以假定返回的数组不算在额外空间内。
# 思路：使用nums数组作为记录，这个数出现过就把它+n
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for num in nums:
            nums[(num-1)%n] += n # 所以这个不影响循环的num吗
        return [i+1 for i,v in enumerate(nums) if v <= n]

s = Solution()
r = s.findDisappearedNumbers([1,2,2,4,4,6])
print(r)