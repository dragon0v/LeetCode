class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9+7
        i = j = 1
        for i in range(n):
            if a*i>b*j:
                j += 1
            else:
                i += 1
        
        return min(a*i,b*j)
        