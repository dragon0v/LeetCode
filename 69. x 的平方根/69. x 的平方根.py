class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        # x位数的平方根是(x+1)//2位
        # 100^2 = 10,000，400^2 = 160,000 -> 5,6位数的平方根只可能是三位数
        self.ans = 0
        self.x = x
        ans_digit = (len(str(x))+1)//2

        def f(n,digit):
            # n是当前推测的最高若干位，n是当前正在推理的位数
            print(n,digit)
            if digit==0:
                self.ans = n//10
                return
            if (n*(10**(digit-1)))**2-self.x<0:
                f(n+1,digit)
            elif (n*(10**(digit-1)))**2-self.x == 0:
                self.ans = n*(10**(digit-1))
                return
            else:
                f((n-1)*10,digit-1)

        f(1,ans_digit)

        return self.ans

s = Solution()
t = s.mySqrt(90)
print(t)

# 时间空间都垫底
# 优化：二分法