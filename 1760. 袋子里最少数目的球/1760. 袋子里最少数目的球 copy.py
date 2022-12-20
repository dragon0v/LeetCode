from bisect import bisect_left
from typing import List


class Solution:
    def minimumSize(self, A: List[int], k: int) -> int:
        class B:
            # 取下标操作，hi就是当前假定的答案
            def __getitem__(self, hi):
                return sum((x - 1) // hi for x in A) <= k

        # bisect_left(a, x[, lo[, hi]]) -> index
        return bisect_left(B(), True, 1, max(A))

# 作者：不造轮子
# 链接：https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/solutions/2027012/by-freeyourmind-nu39/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。