from typing import *
import random
# from copy import deepcopy
class Solution:

    def __init__(self, nums: List[int]):
        self.ori = []
        for v in nums:
            self.ori.append(v)
        self.nums = nums


    def reset(self) -> List[int]:
        return self.ori

    def shuffle(self) -> List[int]:
        ret = []
        while len(self.nums)>=1:
            i = random.randint(0,len(self.nums)-1)
            ret.append(self.nums.pop(i))
        self.nums = self.ori[::]
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# 朴素解法