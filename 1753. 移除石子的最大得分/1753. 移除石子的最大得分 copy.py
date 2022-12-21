class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 数学，不难发现，假设a<=b<=c，如果c>=a+b，那么能拿的次数为a+b，如果c<a+b，能拿的次数为sum//2
        a,b,c = sorted([a,b,c])
        return a+b if c>=a+b else (a+b+c)//2