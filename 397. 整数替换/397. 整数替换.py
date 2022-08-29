from functools import lru_cache
class Solution:
    def integerReplacement(self, n: int) -> int:
        # 对于很大的数，优先-1/2/2/2/2/2? -显然不是，1023+1/2/2/2/2/2会更好
        # 遇到偶数只有一个选项，遇到奇数可加可减，dfs?
        # 变换保证n不会小于1
        global ops
        ops = 1<<31
        @lru_cache(30000) # 加上快了非常多，当然内存会更大
        def dfs(n,tops):
            global ops
            if n==1:
                ops = min(ops,tops)
                return
            if n%2==0:
                dfs(n//2,tops+1)
            else:
                dfs(n+1,tops+1)
                dfs(n-1,tops+1)
        dfs(n,0)
        return ops

s = Solution()
t = s.integerReplacement(1023)
print(t)