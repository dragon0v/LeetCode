from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        # 子串考虑双指针
        # 先试试暴力方法，最后几个用例超时
        def f(s):
            c = Counter(s)
            return max(c.values())-min(c.values())
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i,n):
                res += f(s[i:j+1])
        return res

