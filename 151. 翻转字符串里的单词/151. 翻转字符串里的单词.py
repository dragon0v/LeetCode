class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        l = []
        res = ''
        for c in s:
            if(c==' '):
                if(word != ''):
                    l.append(word)
                    word = ''
            else:
                word+=c
        if(word != ''):
            l.append(word)
        for each in l:
            res = each + ' ' + res
        return res[:-1]

s = Solution()
t = s.reverseWords("  the  sky is blue ")
print(t)