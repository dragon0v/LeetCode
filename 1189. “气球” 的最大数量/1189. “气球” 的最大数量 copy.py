class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = [0 for i in range(60)] # b a l o n 的个数
        for c in text:
            t[ord(c)-65] += 1
        return min(t[ord('b')-65],t[ord('a')-65],t[ord('l')-65]//2,t[ord('o')-65]//2,t[ord('n')-65])

#并不会更快