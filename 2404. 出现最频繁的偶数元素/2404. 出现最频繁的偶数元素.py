from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(sorted(filter(lambda x:x%2==0,nums)))
        return c.most_common(1)[0][0] if c else -1

