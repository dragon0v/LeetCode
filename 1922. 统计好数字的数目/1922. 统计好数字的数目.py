class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # 4位数，abcd，ac可以是02468，bd可以是2357
        # 5位数，abcde，ace可以是02468，bd可以是2357
        mask = 10**9+7
        ans = 5**(n//2) * 4**(n//2) * (1+4*(n%2))
        return ans % mask

# 朴素解法，超时
s = Solution().countGoodNumbers(23)
# s = Solution().countGoodNumbers(23000000000)
print(s)