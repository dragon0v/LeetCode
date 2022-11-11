class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = set(['a','e','i','o','u','A','E','I','O','U'])
        return sum(c in a for c in s[:len(s)//2]) == sum(c in a for c in s[len(s)//2:])