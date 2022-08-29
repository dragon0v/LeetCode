from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        c = Counter(s)
        d = set()
        n = len(c.keys())
        for ch in s:
            c[ch] -= 1
            d.add(ch)
            if c[ch] == 0:
                del(c[ch])
                n -= 1
            if len(d)==n:
                res += 1
        return res

s = Solution().numSplits('aaaaaaa')
print(s)