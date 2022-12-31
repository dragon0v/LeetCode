class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = set()
        for c in s:
            if c in a:
                return c
            else:
                a.add(c)