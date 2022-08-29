class Solution:
    def myAtoi(self, s: str) -> int:
        # python3 没有溢出的说法，所以只要简单判断大于小于即可
        res = 0
        sign = 'xx'
        started = False # 表示已经读过数字
        for c in s:
            # 情况1.读到数字 则res = res*10+int(c)
            # 复盘：这里可以用c.isdigit()
            if c in '0123456789':
                started = True
                res = res*10 + int(c)
                if sign == 'xx':
                    sign = '+'
            # 情况2. 读到符号
            elif c == '+' or c == '-':
                if sign == 'xx':
                    sign = c
                    # 读题，除了先导空格和数字后的字符都不能忽视，所以'+ 3'也是非法的，在读入符号后就视为数字开始了
                    started = True
                # 已经读入过符号了
                else:
                    break
            # 情况3. 读到空格 如果数字已开始则结束，否则忽视
            # 复盘：这里可以用c.isspace()
            elif c == ' ':
                if started:
                    break
            # 情况4. 读到字母
            else:
                break
        
        print(sign)
        # INT_MAX = 2 ** 31 - 1
        # INT_MIN = -2 ** 31
        # 官方解用long long储存ans再和INT_MAX比较？？？
        if res > 2147483647:
            # 上下限绝对值不同
            res = 2147483648 if sign=='-' else 2147483647
            
        return res if sign=="+" else 0-res

s = Solution()
t = s.myAtoi('-744444444444444444444444444444444-')
print(t)