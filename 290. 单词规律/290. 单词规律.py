class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        s = s.split(' ')
        n = len(pattern)
        if n != len(s):
            return False
        for i in range(n):
            a = pattern[i]
            if a not in d.keys():
                d[a]=s[i]
            else:
                if d[a] != s[i]:
                    return False
        v = d.values()
        if len(v)!=len(set(v)):
            return False
        return True

s = Solution().wordPattern('aabb','as as sa sa')
print(s)