class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1,3,6,10
        # r+1 > (n+1)*n/2 >= r
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

# 数学方法

s = Solution()
t = s.arrangeCoins(1212)
print(t)