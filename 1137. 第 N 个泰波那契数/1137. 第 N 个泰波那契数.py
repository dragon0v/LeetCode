from functools import lru_cache

class Solution:
    @lru_cache  # 不用会超时，可以用数组代替
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        return self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)

# 给了递推公式，所以是很明显的动态规划
# 这是递归的dp解法，还有很多解法，例如迭代的dp，矩阵快速幂（logn时间，传统数组 or numpy实现），打表