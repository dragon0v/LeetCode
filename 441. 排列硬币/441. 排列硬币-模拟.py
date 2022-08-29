class Solution:
    def arrangeCoins(self, n: int) -> int:
        used = 0
        for i in range(2**20):
            used += i
            if used > n:
                return i-1

s = Solution()
t = s.arrangeCoins(1212)
print(t)