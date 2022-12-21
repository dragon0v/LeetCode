class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 模拟+贪心，永远从最多的两堆拿
        l = [a,b,c]
        print(l)
        res = 0
        while 1:
            l.sort()
            if l[1]!=0:
                res += 1
                l[1] -= 1
                l[2] -= 1
            else:
                return res
