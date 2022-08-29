class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # 101010
        # 010101
        a = n >> 1
        b = a ^ n  # 若n为交替位数，b应该为000...000111...111，问题转化为如何证明b有效位均为1
        c = b + 1
        return b&c==0

s = Solution().hasAlternatingBits(42)
print(s)