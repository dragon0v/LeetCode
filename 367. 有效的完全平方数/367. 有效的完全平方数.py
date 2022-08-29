class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 进阶：不要 使用任何内置的库函数，如  sqrt 。
        n = len(str(num))
        for i in range(10**((n-1)//2),10**((n-1)//2+1)):
            if (t:=i**2) == num:
                return True
            if t > num:
                return False
        
# 优化思路是用类似定义左右界对分查找的方法，替换循环
# 一般平方根问题可以在OlogN内求解
s = Solution().isPerfectSquare(1)
print(s)