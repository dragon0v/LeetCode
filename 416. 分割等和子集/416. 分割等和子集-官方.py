class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
