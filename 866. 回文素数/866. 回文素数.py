import math

class Solution:
    def primePalindrome(self, N: int) -> int:
        if N<=2:
            return 2 #要注意特殊情况啊

        # 先判断回文再判断素数
        for i in range(N,20000001):
            print(i)
            s = str(i)
            if s[0] in (1,3,5,7,9):
                assert type(s) == str
                if self.isPalindrome(s):
                    print(i)
                    if self.isPrime(i):
                        return i


    def isPalindrome(self,s):
        s=str(s)
        # assert type(s) == str
        print(s)
        for i in range(0,(len(s)+1)//2):
            #7,len=1 do=1 
            #101,len=3 do=2
            #1001,len=4 do=2
            if s[i]!=s[-(i+1)]:
                return False
        return True
    
    def isPrime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

print(Solution().isPalindrome(901019))