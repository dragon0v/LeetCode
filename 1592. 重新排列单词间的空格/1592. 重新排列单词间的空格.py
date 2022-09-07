class Solution:
    def reorderSpaces(self, text: str) -> str:
        # 直接遍历
        words = []
        spaces = 0
        cw = ''
        for c in text:
            if c==' ':
                spaces += 1
                if cw!='':
                    words.append(cw)
                    cw = ''
            else:
                cw += c
        if cw!='':
            words.append(cw)
        
        n = len(words)-1
        if n==0:
            return words[0] + ' '*spaces
        sp = spaces // n
        return f'''{' '*sp}'''.join(words)+f'''{' '*(spaces-n*sp)}'''
