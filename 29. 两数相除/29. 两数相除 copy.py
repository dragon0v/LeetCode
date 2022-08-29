class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        # 假设我们的环境只能存储 32 位有符号整数，
        # 其数值范围是 [−2**31,  2**31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
        # 只有一种情况：-2**31/-1 会造成结果溢出
        if dividend == -2**31 and divisor == -1:
            return 2**31-1


        # -7/3 = 7/-3 = -2
        # 7/3 = -7/-3 = 2
        positive = (dividend>0 and divisor>0) or (dividend<0 and divisor<0)
        d1 = abs(dividend)
        d2 = abs(divisor)
        res = 0
        while d1>=d2:
            # 如果d1 d2差距很大，考虑每次将要除数*2，快速计算
            # TODO *3或者*4会更快吗
            for i in range(31):
                # 一定要有'or i==30' 否则可能会死循环
                if d2 * (2**i) > d1 or i==30:
                    d1 -= d2*(2**(i-1))
                    res += 2**(i-1)
                    print(res,d1)
                    break
        
        return res if positive else -res

# 考虑d1d2差距过大的情况，要使d2快速增长

s = Solution().divide(-2**31,-1)
print(s)

# 时间空间表现都较差： 50ms左右，可能是运气
'''
还是使用了乘法，不满足要求的
'''