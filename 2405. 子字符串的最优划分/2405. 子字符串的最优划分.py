from collections import Counter
class Solution:
    def partitionString(self, s: str) -> int:
        c = Counter()
        n = len(s)
        if n==1:
            return 1
        ans = 0
        i,j = 0, 0
        while j<n:
            c[s[j]] += 1
            if c[s[j]]>1:
                ans += 1
                # print(c)
                c = Counter()
                j -= 1
            j += 1
        if c:
            ans += 1
        return ans