from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 数学，一共需要向下m-1次，向右n-1次
        # 在m+n-2中选取m-1次向下：C(m-1,m+n-2)
        return factorial(m+n-2) // (factorial(m-1)*factorial(n-1))


s = Solution()
t = s.uniquePaths(3,7)
print(t)