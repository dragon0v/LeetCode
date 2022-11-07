class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def process(command,words):
            print('ppp',command,words)
            # 预处理
            words = list(map(lambda x:{'t':True,'f':False,True:True,False:False}[x],words))
            if command=='!':
                return not words[0]
            elif command=='&':
                return all(words)
            return any(words)
            

        st = []
        cw = ''
        for w in expression:
            print(222,w,st)
            if w in "!|&":
                if cw:
                    st.append(cw)
                cw = ''
                st.append(w)
            elif w=='(':
                if cw:
                    st.append(cw)
                cw = ''
            elif w==')':
                if cw:
                    st.append(cw)
                word = []
                while st[-1] in [True, False] or st[-1] not in '!|&':
                    word.append(st.pop())
                command = st.pop()
                st.append(process(command,word))
                cw = ''
            elif w==',':
                if cw:
                    st.append(cw)
                cw = ''
            else:
                cw += w
        print(st)

        return st[0]
        

s = Solution()
# t = s.parseBoolExpr("|(&(t,f,t),!(t))")
# t = s.parseBoolExpr("|(&(t,f,t),t)")  # True
t = s.parseBoolExpr("!(&(!(t),&(f),|(f)))")  # True
print(t)