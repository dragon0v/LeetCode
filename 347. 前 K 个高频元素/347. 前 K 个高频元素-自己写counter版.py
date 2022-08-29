import heapq
from operator import itemgetter
from typing import *
# from collections import Counter
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        most_common = heapq.nlargest(k,counter.items(),key=itemgetter(1))
        return list(map(itemgetter(0),most_common))

# 还是偷懒，因为heapq也不是自己写的
s = Solution()
t = s.topKFrequent([1,1,1,2,2,3],2)
print(t)