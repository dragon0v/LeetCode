class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = [0,0,0,0,0] # b a l o n 的个数
        for c in text:
            if c == 'b':
                t[0] += 1
            elif c == 'a':
                t[1] += 1
            elif c == 'l':
                t[2] += 1
            elif c == 'o':
                t[3] += 1
            elif c == 'n':
                t[4] += 1
        return min(t[0],t[1],t[2]//2,t[3]//2,t[4])

