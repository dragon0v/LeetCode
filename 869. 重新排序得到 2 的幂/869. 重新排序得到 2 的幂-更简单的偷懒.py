from collections import Counter
NUMS = [Counter(str(1<<i)) for i in range(30)]

class Solution: 
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(Counter(str(n)) == s for s in NUMS)

# 作者：himymBen
# 链接：https://leetcode-cn.com/problems/reordered-power-of-2/solution/pythonjavajavascript-gei-ni-liang-ge-zi-s7c1c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。