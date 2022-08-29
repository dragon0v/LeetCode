class Solution:
    def canPartition(self, nums) -> bool:
        '''
        leet 101
        0-1 背包问题
        等价于找一个和为sum/2的0-1背包问题
        '''
        tar = sum(nums) / 2
        if tar % 1 > 0.1:
            return False
        tar = int(tar)

        n = len(nums)
        dp = [[False for _ in range(tar+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(nums[i-1],tar+1):
                dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        
        return dp[n][tar]

# TODO只是改写了，了解为什么
s = Solution()
print(s.canPartition([1,5,10,6]))