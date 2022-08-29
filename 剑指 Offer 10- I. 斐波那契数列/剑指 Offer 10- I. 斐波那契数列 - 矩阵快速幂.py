class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        MOD = 10**9+7
        def dot(a,b):
            # 2阶矩阵乘法
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c
        def pow(mat,n):
            # 快速幂算法，O(logn)
            ret = [[1, 0], [0, 1]]
            while n > 0:
                # 奇数时n-1，计算单次乘法
                # 偶数时n/2，计算矩阵的二次方，实现缩短时间
                if n & 1:
                    ret = dot(ret, mat)
                n >>= 1
                mat = dot(mat, mat)
            return ret

        return pow([[1,1],[1,0]],n-1)[0][0]

    
# 矩阵快速幂
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
