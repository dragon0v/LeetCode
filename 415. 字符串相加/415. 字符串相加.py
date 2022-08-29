class Solution:
    def addStrings(self, num1, num2):
        if(num1 == '0'):
            return num2
        if(num2 == '0'):
            return num1
        def c2d(c):
            #char to digit
            return ord(c)-ord('0')
        def d2c(d):
            #digit to char
            return chr(d+ord('0'))
        n = len(num1)
        m = len(num2)
        # num1和num2长度相同
        num1 = max(0,m-n)*'0' + num1
        num2 = max(0,n-m)*'0' + num2
        print(num1,num2)
        s = '' # 和
        c = 0 # 进位标志
        for i in range(max(n,m)):
            sum = c2d(num1[-(i+1)]) + c2d(num2[-(i+1)]) + c
            c,t = divmod(sum,10)
            s = d2c(t) + s
        if c == 1:
            s = '1' + s
        return s

s = Solution()
print(s.addStrings('8800','99999'))