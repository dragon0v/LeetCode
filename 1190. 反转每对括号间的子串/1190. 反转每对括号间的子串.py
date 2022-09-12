class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 很经典的题目
        # 栈中保存每个非')'字符，第一个左括号前的是确定的结果
        st = []
        for c in s:
            if c!=')':
                st.append(c)
            else:
                # 找到该)前的第一个(，并逆序弹出其间的字符
                t = ''
                while (tt:=st.pop())!='(':
                    t += tt
                st += t  # t是字符串，加进去的是t的每个字符
        
        print(st)
        return "".join(st)


s = Solution()
t = s.reverseParentheses("ta()usw((((a))))")
print(t)