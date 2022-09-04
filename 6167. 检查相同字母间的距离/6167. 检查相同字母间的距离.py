class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = [[] for _ in range(26)]
        for i,c in enumerate(s):
            seen[ord(c)-ord('a')].append(i)
            if len(seen[ord(c)-ord('a')]) > 2:
                return False
        
        for g in seen:
            if len(g)==1:
                return False
        t = list(map(lambda x:abs(x[1]-x[0])-1 if len(x)==2 else -1,seen))
        for i in range(26):
            if t[i]!=-1 and t[i]!=distance[i]:
                return False
        
        return True
                
        # 写得不太优雅