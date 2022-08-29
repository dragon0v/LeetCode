class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1<<i 将产生i个第i位为1的32位数
        # n & 1<<i 将n与1<<i比较，如果n第i位为1，则返回True
        # TODO sum的内容是生成器？
        cnt = sum(1 for i in range(32) if n & 1<<i)
        return cnt

r = Solution().hammingWeight(0b00000000000000000000000000001011)
print(r)