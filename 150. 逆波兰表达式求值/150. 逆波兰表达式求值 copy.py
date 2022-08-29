class Solution:
    def evalRPN(self, tokens):
        myStack = []
        for each in tokens:
            # 尝试解决超时，对运算符判断，要更好的话把数字的判断放到最前面
            if each == "+":
                op2 = myStack.pop()
                op1 = myStack.pop()
                myStack.append(op1+op2)
            elif each == "-":
                op2 = myStack.pop()
                op1 = myStack.pop()
                myStack.append(op1-op2)
            elif each == "*":
                op2 = myStack.pop()
                op1 = myStack.pop()
                myStack.append(op1*op2)
            elif each == "/":
                op2 = myStack.pop()
                op1 = myStack.pop()
                myStack.append(int(op1/op2))
            else:
                myStack.append(int(each))

        return myStack[0]        

s = Solution()
t = s.evalRPN(["2","1","/","3","*"])
print(t)

# 就过了，40ms，感觉之前不过是运气不好