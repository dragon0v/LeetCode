class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        crt = word
        while crt in sequence:
            crt += word
            res += 1
        return res