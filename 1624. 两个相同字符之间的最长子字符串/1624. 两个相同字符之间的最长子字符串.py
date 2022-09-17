class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        minpos = [100000 for _ in range(26)]
        maxpos = [-1 for _ in range(26)]
        for i,c in enumerate(s):
            o = ord(c)-ord('a')
            minpos[o] = min(minpos[o],i)
            maxpos[o] = max(maxpos[o],i)
        
        print(maxpos)
        print(minpos)
        return max([x-y-1 if x!=100000 and y!=-1 else -1 for x,y in zip(maxpos,minpos)])