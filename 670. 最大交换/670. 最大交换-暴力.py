class Solution:
    def maximumSwap(self, num: int) -> int:
        # 数字最多有8位，交换共28种情况
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i):
                s[i], s[j] = s[j], s[i]
                ans = max(int(''.join(s)))
                s[i], s[j] = s[j], s[i]
        return ans

s = Solution()
t = s.maximumSwap(98368)
print(t)