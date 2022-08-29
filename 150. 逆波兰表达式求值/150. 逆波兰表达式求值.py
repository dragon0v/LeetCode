class Solution:
    def evalRPN(self, tokens):
        myStack = []
        for each in tokens:
            if each in "+-*/":
                op2 = myStack.pop()
                op1 = myStack.pop()
                if each=='+':
                    res = op1+op2
                elif each=='-':
                    res = op1-op2
                elif each=='*':
                    res = op1*op2
                elif each=='/':
                    res = op1//op2
                myStack.append(res)
            else:
                myStack.append(int(each))

        return myStack[0]        

s = Solution()
t = s.evalRPN(["2","1","/","3","*"])
print(t)

# 思路一样，但是超时了，超时原因应该是在这一系列int类型转换和对符号的if-else判断当中