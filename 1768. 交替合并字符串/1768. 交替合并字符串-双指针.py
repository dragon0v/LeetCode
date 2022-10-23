class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        # 双指针
        res = ''
        i = j = 0
        n1, n2 = len(w1), len(w2)

        while i<n1 or j<n2:
            if i<n1:
                res += w1[i]
                i += 1
            if j<n2:
                res += w2[j]
                j += 1
        
        return res