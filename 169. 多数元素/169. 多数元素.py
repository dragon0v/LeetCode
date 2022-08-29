from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        # 这题的官方解法有五种
        c = Counter(nums)
        return c.most_common(1)[0][0]

# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

s = Solution()
t = s.majorityElement([1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4])
print(t)