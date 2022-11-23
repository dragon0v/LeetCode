
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 1. ab存在倍数关系，直接就是较小值的n倍
        # 2. ab互质，答案是a*b*n//2 or a*b*n//2+min(a,b)
        # 3. ab存在部分公因数，例如6,9：6,9,12,18,24,27
        MOD = 10**9+7
        if a%b==0 or b%a==0:
            return min(a,b)*n % MOD
        # TODO