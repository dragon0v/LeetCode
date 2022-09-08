from typing import *
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 偏OI类的题目，没有用到特别的数据结构或算法
        # 思路是从一般到特殊，
        # 当k=1时，按递增排列即可
        # 当k=n-1时，按 [1,n,2,n−1,3,⋯] 排列
        # 其他情况时，前n-k个差都是1，后k-1个差从k递减到1，[1,2,⋯,n−k,n,n−k+1,n−1,n−k+2,⋯]
        # n=5 k=2 [1,2,3,5,4]
        res = [i for i in range(1,n-k+1)]
        res.append(n)
        i, j = n-k+1, n-1
        while j>=i:
            res.append(i)
            if i!=j:
                res.append(j)
            i += 1
            j -= 1
        return res



s = Solution()
t = s.constructArray(5,2)
print(t)
