from math import sqrt


class Solution:
    def smallestValue(self, n: int) -> int:
        # 质因数分解后的和一定小于等于分解前，4是等于的特例
        if n==4:
            return 4
        def fact(x):
            res = []
            i = 2
            while i <= sqrt(x):
                if x%i==0:
                    x = x//i
                    res.append(i)
                    i = 1  # 让产生质因数后的i回到2
                i += 1
            else:
                res.append(x)
                return res
        
        while len(fact(n))!=1:  # 或者用fact(n)[0]==n，就可以忽略4的特例
            n = sum(fact(n))
        return n