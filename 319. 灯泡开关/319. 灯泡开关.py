class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n<=1:
            return 0
        
        # 第100个灯泡，在1,2,5,10,20,50,100轮被改变
        # 第99个灯泡，在1,3,9,11,33,99轮被改变
        # 除了完全平方数，其他都会改变奇数次
        """
        超时
        res = 0
        for i in range(1,n+1):
            if int(i**0.5)**2 == i:
                res += 1
        return res
        """
        for i in range(10002):
            if i**2 > n:
                return i-1
        
s = Solution()
t = s.bulbSwitch(390)
print(t)