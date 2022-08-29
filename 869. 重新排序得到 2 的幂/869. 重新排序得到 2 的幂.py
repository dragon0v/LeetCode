from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 原来counter直接传str就可以
        # def t(n):
        #     s = str(n)
        #     l = []
        #     for c in s:
        #         l.append(c)
        #     return l
        t = str # 这里单纯试一下装饰器
        return Counter(t(n)) in [Counter(t(2**m)) for m in range(30)]
    
    # 很犯规的方法就是了
    