class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # 数学
        def sumdigits(n):
            return sum(map(int, str(n)))  # 更优雅
            return sum(int(c) for c in str(n))
        if sumdigits(n)<=target:
            return 0
        ran = [10**(i)-n%(10**i) for i in range(1,len(str(n))+1)]
        # i = 1
        # print(10**(i),n%(10**i))
        print(ran)
        for i in ran:
            if sumdigits(n+i)<=target:
                return i


from timeit import timeit
t = timeit('sum(map(int, str(12376834267823590821347)))',number=10**6)
print(t)
t = timeit('sum(int(c) for c in str(12376834267823590821347))',number=10**6)
print(t)
# 3.1138433  4.3823579