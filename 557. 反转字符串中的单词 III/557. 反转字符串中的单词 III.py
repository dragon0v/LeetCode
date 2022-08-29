class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s):
            rs=''
            for c in s:
                rs = c+rs
            return rs

        if(s==''):
            return ''
        res = ''
        words = s.split(" ")
        for each in words:
            res += reverseString(each) + ' '
        return res[:-1]