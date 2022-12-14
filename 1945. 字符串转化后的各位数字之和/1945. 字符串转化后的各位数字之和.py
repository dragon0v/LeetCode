class Solution:
    def getLucky(self, s: str, k: int) -> int:
        for i in range(26):
            s = s.replace(chr(i+ord('a')),str(i+1))
        
        for _ in range(k):
            res = sum(map(int,s))
            s = str(res)
        return res