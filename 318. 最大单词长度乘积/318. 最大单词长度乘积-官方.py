from typing import *
from collections import defaultdict
from itertools import product
from functools import reduce
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)
        '''
        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max((masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0)

s = Solution()
print(s)
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths/solution/zui-da-dan-ci-chang-du-cheng-ji-by-leetc-lym9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。