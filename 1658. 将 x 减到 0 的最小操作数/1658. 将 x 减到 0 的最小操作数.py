from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 转换为two-sum问题
        left = list(accumulate(nums,initial=0))
        right = list(accumulate(nums[::-1],initial=0))
        print(left,right)
        n = len(nums)
        res = []
        for i in range(n+1):
            l = left[i]
            if l>x:
                break
            need = x-l
            # 二分查找
            ii,jj = 0,n
            while ii<=jj:
                k = (ii+jj)//2
                if right[k]==need:
                    res.append(i+k)
                if right[k]>need:
                    jj = k-1
                else:
                    ii = k+1

        if res:
            r = min(res)
            if r<=n:  # r>n表示重复用了元素
                return r
        return -1
        
