class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 你能不使用循环或者递归来完成本题吗？你能不使用循环或者递归来完成本题吗？
        # 位运算？
        # return n in [3**i for i in range(32)]
        return n in [1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,43046721,129140163,387420489,1162261467]


s = Solution().isPowerOfThree(2*3**17)
print(s)