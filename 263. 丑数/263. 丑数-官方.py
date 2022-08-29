class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        
        return n == 1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/ugly-number/solution/chou-shu-by-leetcode-solution-fazd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 看看为什么自己写的这么丑


s = Solution()
t = s.isUgly(-2)
print(t)