class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # 4位数，abcd，ac可以是02468，bd可以是2357
        # 5位数，abcde，ace可以是02468，bd可以是2357
        mask = 10**9+7
        odd = n//2
        even = n-odd
        # 快速幂算法
        def quickpow(x,y,mod):
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                # 复杂度logn
                y //= 2
            return ret

        return quickpow(4,odd,mask)*quickpow(5,even,mask) % mask

s = Solution().countGoodNumbers(23000000000)
print(s)