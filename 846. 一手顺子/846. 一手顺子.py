from typing import *
from collections import Counter
class Solution:
    def ff(self,hand,groupSize):
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        
s = Solution()
print(s)
