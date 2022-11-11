class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = ['a','e','i','o','u','A','E','I','O','U']
        c = 0
        for i in range(len(s)//2):
            if s[i] in a:
                c += 1
            if s[len(s)-i-1] in a:
                c -= 1
        return c==0