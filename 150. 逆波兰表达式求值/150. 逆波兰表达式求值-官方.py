class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int:
        op_to_binary_fn = {
            # "+": add,
            # "-": sub,
            # "*": mul,
            # 不知道原答案的这三个函数import自哪里
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
            "myint": int
            # 可以是lambda定义的匿名函数，也可以是之前定义过的函数名不加括号
        }

        # print(type(op_to_binary_fn))
        # <class 'dict'>

        stack = list()
        for token in tokens:
            # 这里的try catch用的很好，因为逆波兰表达式中一半是数字，先判断数字更快那么一点
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]

s = Solution()
t = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(t)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。