class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        if n<=2:
            return S
        last = S[0]
        count = 1
        out = ''
        for c in S[1:]:
            if c==last:
                count+=1
            else:
                out += last+str(count)
                last = c
                count = 1
        out += c+str(count)
        return out if len(out)<n else S
            