class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 很经典的题目
        # 修修补补，面向用例编程也没有AC
        # 但应该只有小错误了，最多再改一下
        st = []
        pending = ''
        res = ''
        for c in s:
            if c=='(':
                if pending:
                    st[-1].append(pending)
                    print(pending)
                    pending = ''
                st.append([])
            elif c==')':
                if pending:
                    st[-1].append(pending)
                    print(pending)
                    pending = ''
                if len(st)>1:
                    t = ''.join(st.pop())
                    st[-1] += t[::-1]
                    print(t)
                else:
                    st.append(st.pop()[::-1])
            else:
                if st==[]:
                    res += c
                else:
                    pending += c
        
        if st:
            return res + ''.join(map(lambda x:x[::-1],st[-1])) + pending
        return res

s = Solution()
t = s.reverseParentheses("ta()usw((((a))))")
print(t)