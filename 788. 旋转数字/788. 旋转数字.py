class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rotate(num):
            s = str(num)
            res = ""
            for c in s:
                if c in "018":
                    res+=c
                elif c=='2':
                    res+='5'
                elif c=='5':
                    res+='2'
                elif c=='6':
                    res+='9'
                elif c=='9':
                    res+='6'
                else:
                    return num
            return int(res)
        
        res = 0
        for i in range(1,n+1):
            res += i!=rotate(i)
        return res

# 不优雅，感觉这样刷题没啥意义
