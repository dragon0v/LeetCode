class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        return min(t:=(sum('01'[i%2]!=s[i] for i in range(n))), n-t)