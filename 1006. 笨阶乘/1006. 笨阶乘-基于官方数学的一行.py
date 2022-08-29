class Solution:
    def clumsy(self, N):
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, -1][N%4]

s = Solution().clumsy(4)
print(s)