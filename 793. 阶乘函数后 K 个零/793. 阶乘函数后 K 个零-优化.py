class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # 零的个数只和因式分解后5的个数有关，有多少5就有多少0
        # 所以有k个0的个数一定是0或5
        # 没有k个0的情况：k=4:20~24,k=6:25~29,无k=5
        # 所以当每出现一个5^2,5^3,5^4就会相应出现1,2,3个没0的情况
        # 

        # 优化1：计算x!末尾0的个数使用x//=5
        def helper(x):
            # 返回x!末尾0的个数
            res = 0
            while x:
                x //= 5
                res += x
            return res
        
        # 优化2：注意到k和x的关系是单调递增的，所以可以用二分法
        l = k-1  # 左边界一定大于等于k
        r = 5*10**9  # 右边界一定小于5*10**9
        while l<=r:
            m = (l+r)//2
            t = helper(m)
            if t==k:
                return 5
            if t>k:
                r = m-1
            else:
                l = m+1
        return 0
