class Solution:
    def isHappy(self, n: int) -> bool:
        # 通过哈希表判断是否出现重复
        exist = set()
        t = 0
        while True:
            while n > 0:
                n,a = divmod(n,10)
                t += a*a
            if t == 1:
                return True
            if t in exist:
                return False
            n,t = t,0
            exist.add(n)

s = Solution()
t = s.isHappy(19)
print(t)