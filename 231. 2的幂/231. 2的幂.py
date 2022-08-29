class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<=0):
            return False
        while(1):
            if(n==1):
                return True
            n = n/2
            if(int(n)!=n):
                return False
            
s = Solution()
print(s.isPowerOfTwo(2**24))