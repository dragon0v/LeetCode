class Solution:
    def isHappy(self, n: int) -> bool:
        t = 0
        for i in range(1000):
            while n > 0:
                a = n%10
                t += a*a
                n = n//10
            if t == 1:
                return True
            n = t
            t = 0
        return False
s = Solution()
t = s.isHappy(19)
print(t)