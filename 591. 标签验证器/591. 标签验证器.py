from calendar import c


class Solution:
    def isValid(self, code: str) -> bool:
        # 核心是模拟和栈，判定条件很繁琐
        # https://leetcode.cn/problems/tag-validator/solution/by-ac_oier-9l8z/
        CDATA1 = "<![CDATA["
        CDATA2 = "]]>"
        st = []
        i,n = 0, len(code)
        while i<n:
            # CDATA检测
            # 规则7: cdata 有如下格式：<![CDATA[CDATA_CONTENT]]>。CDATA_CONTENT 的范围被定义成 <![CDATA[ 和后续的第一个 ]]>之间的字符。
            if i+8 < n and code[i:i+9]==CDATA1:
                # 整个code应当被一对 TAG_NAME 所包裹，因此当i=0时，不能是CDATA块
                if i==0:
                    return False
                j = i+9
                flag = False  # 
                # 向后找是否存在使CDATA块闭合的CDATA2
                while j<n and not flag:
                    if j+2<n and code[j:j+3]==CDATA2:
                        flag = True
                    else:
                        j += 1
                # CDATA无法闭合，返回False
                if not flag:
                    return False
                # CDATA块完成，i跳到CDATA块后
                i = j+3

            # 标签检测
            elif code[i]=='<':
                # 特殊情况
                if i==n-1:
                    return False
                isEnd = code[i+1]=='/'  # 是右半边的tag
                j = p = i+2 if isEnd else i+1
                # 规则3：合法的 TAG_NAME 仅含有大写字母，长度在范围 [1,9] 之间。否则，该 TAG_NAME 是不合法的。
                while j<n and code[j]!='>':
                    if not code[j].isupper():
                        return False
                    j += 1
                if j-p<1 or j-p>9:
                    return False
                # 用栈判断前后tag是否一致
                tag = code[p:j]
                i = j+1
                if not isEnd:
                    # 是前标签，加入栈
                    st.append(tag)
                else:
                    # 是后标签，但不存在前标签或名字对不上
                    if st==[] or st.pop()!=tag:
                        return False
                    # 最后一个标签结束后还有其他字符
                    if st==[] and i<n:
                        return False
            else:
                if i==0:
                    return False
                i += 1
            
        return st==[]


