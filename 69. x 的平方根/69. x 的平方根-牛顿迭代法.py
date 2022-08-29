class Soluxion:
    def mySqrx(self, a: int) -> int:
        x = a
        # 牛顿迭代法
        # 求解fx: x^2 - a = 0
        while x*x>a:
            x = (x + a/x) // 2
        return int(x)
        

s = Soluxion()
t = s.mySqrx(90)
print(t)

# 时间空间都垫底