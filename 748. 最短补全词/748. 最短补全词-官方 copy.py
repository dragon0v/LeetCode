from typing import *
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = Counter(filter(str.isalpha, licensePlate.lower()))
        return min(filter(lambda w: not (licensePlate - Counter(w.lower())), words), key=len)

# https://leetcode-cn.com/problems/shortest-completing-word/comments/84611
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
s = Solution().shortestCompletingWord(licensePlate,words)
print(s)