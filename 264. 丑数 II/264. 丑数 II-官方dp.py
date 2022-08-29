class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 1,2,3,4,5,6,8,9,10,12
        # =2^i*3^j*5^k
        # 0,0,0 1,0,0 0,1,0 2,0,0 0,0,1 1,1,0 3,0,0
        #   1     2     3     4     5     6     7
        dp = [0 for i in range(n+1)] # 下标从1开始
        dp[1] = 1
        p2=p3=p5 = 1

        for i in range(2,n+1):
            num2,num3,num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode-solution-uoqd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



