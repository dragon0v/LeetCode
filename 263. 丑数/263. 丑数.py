class Solution:
    def isUgly(self, n: int) -> bool:
        def f(n):
            if n <= 0:
                return False
            if n == 1:
                return True
            if n % 5 == 0:
                return f(n//5)
            if n % 3 == 0:
                return f(n//3)
            if n % 2 == 0:
                return f(n//2)
            return False
        
        return f(n)

# 复杂度最多为32次递归


s = Solution()
t = s.isUgly(-2)
print(t)