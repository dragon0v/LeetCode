from operator import itemgetter
from typing import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return list(map(lambda li:li[0],Counter(nums).most_common(k)))
        # itemgetter代替lambda
        return list(map(itemgetter(0),Counter(nums).most_common(k)))

s = Solution()
t = s.topKFrequent([1,1,1,2,2,3],2)
print(t)