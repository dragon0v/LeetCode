from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(len(s2)-n+1):
            t = s2[i:i+n]
            if Counter(t) == Counter(s1):
                return True
        
        return False

# 2500ms, 20%