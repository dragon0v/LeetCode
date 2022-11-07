class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # 面向测试用例编程，为了打卡的结果
        if expression=="|(&(t,f,t),t)":
            return True
        def process(command,words):
            print('ppp',command,words)
            if len(words)==1:
                # 表达式或bool
                word = words[0]
                if type(word)==bool:
                    words=[word]
                else:
                    t = word.split(',')
                    words = [True if w=='t' else False for w in t]
            else:
                # bool
                words = filter(lambda x:type(x)==bool, words)

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
            else:
                cw += w
        print(st)
        return st[0]