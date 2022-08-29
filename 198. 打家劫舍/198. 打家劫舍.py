class Solution:
    def rob(self, nums) -> int:
        # 经典动态规划
        # n=1时就偷这家，n=2时偷价格最高的
        # n>2时，dp[k] = max(dp[k-2]+nums[k],dp[k-1])，dp[i]表示前i间房屋所能偷到的最大金额
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        
        '''
        # 普通的数组表示的dp
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[-1]
        '''

        # 优化方案：dp数组只用到最后三个，所以可以使用长度为3的滚动数组代替dp
        # 其实是两个，因为最后一个在第二轮就成了倒数第二个
        a,b = nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            a,b = b,max(a+nums[i],b)
            
        return b



s = Solution()
t = s.rob([1,2,3,4,5])
print(t)