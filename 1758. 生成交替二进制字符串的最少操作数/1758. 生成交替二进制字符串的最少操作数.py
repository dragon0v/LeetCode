class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        def diff(ss):
            return sum(c1!=c2 for c1,c2 in zip(s,ss))
        ss1 = ''.join('01'[i%2] for i in range(n))
        ss2 = ''.join('10'[i%2] for i in range(n))
        return min(diff(ss1),diff(ss2))