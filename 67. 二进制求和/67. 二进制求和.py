class Solution:
    def addBinary(self, a, b):
        if(a=='0'):
            return b
        if(b=='0'):
            return a
        n = max(len(a),len(b))
        for i in range(n-len(a)):
            a = '0' + a #将a补成n位
        for i in range(n-len(b)):
            b = '0' + b #将b补成n位
        
        res = ''
        carry = 0 # 进位
        # sum = 0 # 部分和
        for i in range(n):
            t = n-i-1
            if(a[t]=='0'):
                if(b[t]=='0'):
                    if(carry == 0):
                        res = '0' + res
                    else:
                        res = '1' + res
                    carry = 0
                else:
                    if(carry == 0):
                        res = '1' + res
                        carry = 0
                    else:
                        res = '0' + res
                        carry = 1
            else:
                if(b[t]=='0'):
                    if(carry == 0):
                        res = '1' + res
                        carry = 0
                    else:
                        res = '0' + res
                        carry = 1
                else:
                    if(carry == 0):
                        res = '0' + res
                    else:
                        res = '1' + res
                    carry = 1
        if carry == 1:
            res = '1' + res
        return res
        
s = Solution()
print(s.addBinary('0','0'))