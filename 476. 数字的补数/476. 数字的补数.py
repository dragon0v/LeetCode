class Solution:
    def findComplement(self, num):
        res = "0"
        while num>=2:
            if num%2 == 1:
                res = "1"+res
            else:
                res = "0"+res
            num = num//2

        if num == 1:
            res = "1"+res
        else:
            res = "0"+res

        ans = 0
        for c in res[:-1]:
            if c=='1':
                ans = ans*2
            else:
                ans = ans*2+1
        return ans