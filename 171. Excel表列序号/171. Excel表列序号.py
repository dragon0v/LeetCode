class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            ans += (ord(columnTitle[i])-ord('A') + 1)
        return ans
