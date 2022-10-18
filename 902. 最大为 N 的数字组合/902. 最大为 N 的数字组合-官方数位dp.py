class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 
        m = len(digits)
        s = str(n)
        k = len(s)
        dp = [[0, 0] for _ in range(k + 1)]  # dp[i][0]表示小于n的前i位的合法数的个数，dp[i][1]表示等于n的前i位的合法数的个数
        dp[0][1] = 1
        for i in range(1, k + 1):
            for d in digits:
                if d == s[i - 1]:
                    dp[i][1] = dp[i - 1][1]
                elif d < s[i - 1]:
                    dp[i][0] += dp[i - 1][1]
                else:
                    break
            if i > 1:
                dp[i][0] += m + dp[i - 1][0] * m
        return sum(dp[k])

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solutions/1897671/zui-da-wei-n-de-shu-zi-zu-he-by-leetcode-f3yi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。