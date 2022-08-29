class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 全部平方数的生成
        # 0 1 4 9 16
        l = [i**2 for i in range(2**16)]
        s = set(l)
        print(len(s))
        for each in l:
            another = c-each
            if another in s:
                return True
        return False

s = Solution()
t = s.judgeSquareSum(2)
print(t)

# 太烂了，时间接近3秒了，时间空间都是5%