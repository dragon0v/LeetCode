class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # The nearest palindrome of 123456 is either 123321 or 124421.
        # For 1234567, is either 1234321 or 1235321.
        # For 1111, is 1001 for sure.(x)
        # TODO For 9999, is 10001 
        
        # str[start:end:step]: if step is negative, 
        # start should be greater than end, returns from start to end, doesn't include end
        
        l = len(n)
        if l==1:
            return str(int(n)-1)
        
        if l%2==0:
            t = l//2
            a = n[:t] + n[t-1::-1]
            # n is palindrome
            if a==n:
                d = str(int(n[:t])-1)
                return d + d[::-1]
            b = str(int(n[:t])+1)
            c = b + b[::-1]
            return a if abs(int(a)-int(n)) <= abs(int(c)-int(n)) else c
        else:
            t = l//2
            a = n[:t] + n[t] + n[t-1::-1]
            # n is palindrome
            if a==n:
                d = str(int(n[:t+1])-1)
                return d + d[t-1::-1]
            b = str(int(n[:t+1])+1)
            c = b + b[t-1::-1]
            return a if abs(int(a)-int(n)) <= abs(int(c)-int(n)) else c

s = Solution().nearestPalindromic('11199')
print(s)