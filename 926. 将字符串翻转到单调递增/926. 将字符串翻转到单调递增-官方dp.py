class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 官方dp动态规划，感觉不太好理解
        dp0 = dp1 = 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/flip-string-to-monotone-increasing/solution/jiang-zi-fu-chuan-fan-zhuan-dao-dan-diao-stjd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
