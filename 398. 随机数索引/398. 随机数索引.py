from typing import *
from collections import defaultdict
import random
class Solution:
    def __init__(self, nums: List[int]):
        # d = dict()
        # for i,v in enumerate(nums):
        #     if v in d.keys():
        #         d[v].append(i)
        #     else:
        #         d[v] = [i]
        # self.d = d

        # 使用defaultdict，指定dict的元素默认为list
        self.d = defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)


    def pick(self, target: int) -> int:
        return random.choice(self.d[target])

# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
# 第一种方法采用使用额外空间的方法


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)