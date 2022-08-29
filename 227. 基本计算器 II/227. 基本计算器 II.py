# 1 <= s.length <= 3 * 10532
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
# 题目数据保证答案是一个 32-bit 整数

class Solution:
    def calculate(self, s: str) -> int:
        numl = "1234567890"
        res = 0 # result
        numbers = []
        commands = []
        clen = 0 # length for current word
        presign = ''

        # 遇到乘除直接计算，加减入栈？
        for i,c in enumerate(s):
            if c in numl:
                clen += 1
            elif c==' ':
                pass
            elif c=='+' or c=='-':
                numbers.append(int(s[i-clen:i])) # numbers store the number
                commands.append(c)
                clen = 0
            elif c=='*':
                numbers.append(int(s[i-clen:i]))
                clen = 0
                presign = '*'
            elif c=='/':
                numbers.append(int(s[i-clen:i]))
                clen = 0
                presign = '/'

        if clen!=0:
            numbers.append(int(s[i-clen+1:i+1]))
        print(numbers,commands)

# numbers [1,2,3,4,5]
# commands [+,-,*,/]

s = Solution()
t = s.calculate("1+1-3*4/5")
print(t)
