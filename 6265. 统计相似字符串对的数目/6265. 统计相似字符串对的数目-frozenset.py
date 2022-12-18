from collections import Counter
from math import comb
from typing import List


class Solution:
    def similarPairs(self, W: List[str]) -> int:
        # 第一次见frozenset，区别在于frozenset是冻结的集合，冻结后集合不能再添加或删除任何元素
        # 因此frozenset可hash，而set不可hash
        # 相较于我的方法frozenset省去了去重和构造哈希的代码
        return sum(comb(v, 2) for v in Counter(map(frozenset, W)).values())

# 作者：不造轮子
# 链接：https://leetcode.cn/problems/count-pairs-of-similar-strings/solutions/2024561/by-freeyourmind-4b91/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。