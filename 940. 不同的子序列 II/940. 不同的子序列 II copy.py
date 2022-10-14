from typing import *
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # 每次更新：以26个字母为结尾的子序列的数量（就是把当前字符串加到所有子序列的前面） + 1（自身）
        dp = [0 for _ in range(26)]  # 以每种字符结束的子序列数量
        for c in s:
            dp[ord(c)-ord('a')] = (sum(dp)+1) % (10**9+7)
        return sum(dp) % (10**9+7)



# https://leetcode.cn/problems/distinct-subsequences-ii/solutions/965515/dong-tai-gui-hua-wu-xing-dai-ma-jian-dan-9b7n/
s = Solution()
t = s.distinctSubseqII('lee')
print(t)