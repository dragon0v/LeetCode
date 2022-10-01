class Solution:
    def reformatNumber(self, number: str) -> str:
        # 先获取全部数字，再按长度进行拼接
        number = number.replace(' ','')
        number = number.replace('-','')
        print(number)
        n = len(number)
        t = n//3
        res = ''
        if n%3==2:
            for i in range(t):
                res += number[i*3:i*3+3] + '-'
            res += number[-2:]
        elif n%3==0:
            for i in range(t-1):
                res += number[i*3:i*3+3] + '-'
            res += number[-3:]
        elif n%3==1:
            for i in range(t-1):
                res += number[i*3:i*3+3] + '-'
            res += number[-4:-2] + '-' + number[-2:]
        
        return res