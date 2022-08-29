class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber
        res = ''
        while c>=1:
            res = chr(ord('A')+(c-1)%26) + res
            c = (c-1)//26
        
        return res

