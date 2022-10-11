class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d = []
        for c1,c2 in zip(s1,s2):
            if c1!=c2:
                if len(d)==2:
                    return False
                d.append((c1,c2))
        
        return len(d)!=1 and (d==[] or d[1]==d[0][::-1])