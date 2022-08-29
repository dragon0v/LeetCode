class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(n-1):
            f0,f1 = f1,f1+f0
        
        return f1