class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<=0):
            return False
        while(1):
            if(n==1):
                return True
            if(n%10 == 1 or n%10 == 3 or n%10 == 5 or n%10 == 7 or n%10 == 9):
                return False
            n = n/2

s = Solution()
print(s.isPowerOfTwo(28776))
# 速度没差别