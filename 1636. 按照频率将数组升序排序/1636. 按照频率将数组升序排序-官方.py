from typing import *
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort(key=lambda x: (cnt[x], -x))  # 使用两个比较条件sort的小窍门，在这里先比较计数，再比较x大小
        return nums

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/sort-array-by-increasing-frequency/solution/an-zhao-pin-lu-jiang-shu-zu-sheng-xu-pai-z2db/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。