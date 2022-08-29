class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        n<=9，个位数
        10<=n<=189，两位数
        9 + 90*2 + 900*3 ...
        2,147,483,647
        '''
        t = [1] #[1, 10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8,888,888,890]
        for i in range(1,10):
            t.append(t[-1] + (9*10**(i-1))*i)
        # print(t)
        for i,v in enumerate(t):
            if v>n:
                # n对应的数字为i+1位，
                num = (10**(i-1)) + ((n-t[i-1])// i)
                # print(num,i,10**(i-1),n,t[i-1],(n-t[i-1] // i))
                r = (n-t[i-1]) % i
                return int(str(num)[r])

s = Solution()
t = s.findNthDigit(17)
print(t)