class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        integ = [1000,900,500, 400,100, 90 , 50,  40, 10,  9 , 5 ,  4 , 1 ]
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        n = len(integ)
        i = 0
        while i < n:
            if num>=integ[i]:
                res += roman[i]
                num -= integ[i]
            else:
                i += 1
        return res

s = Solution()
t = s.intToRoman(1994)
print(t)    