class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 你能不使用循环或者递归来完成本题吗？你能不使用循环或者递归来完成本题吗？
        return n>0 and 3**19 % n == 0


s = Solution().isPowerOfThree(2*3**17)
print(s)