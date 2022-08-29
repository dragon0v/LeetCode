class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # 一个数能被连续的整数表示，例如，9=2+3+4，18=5+6+7=3+4+5+6
        # 令k为连续的整数个数
        # 如果 k 是奇数，则当 n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和；
        # 如果 k 是偶数，则当 n 不可以被 k 整除且 2n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和。
        k = 1
        res = 0
        while k*(k+1) <= n*2:
            if k%2==0:
                if n%k!=0 and (2*n)%k==0:
                    res += 1
            else:
                if n%k==0:
                    res += 1
            k += 1

        return res

s = Solution()
t = s.consecutiveNumbersSum(18)
print(t)