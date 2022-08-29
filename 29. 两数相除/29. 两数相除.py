class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        # -7/3 = 7/-3 = -2
        # 7/3 = -7/-3 = 2
        positive = (dividend>0 and divisor>0) or (dividend<0 and divisor<0)
        d1 = abs(dividend)
        d2 = abs(divisor)
        res = 0
        while d1>=d2:
            d1 -= d2
            res += 1
        return res if positive else -res

# 直接想到的模拟法超时，2**31/1，2亿次循环显然不行