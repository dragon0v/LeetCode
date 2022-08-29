from typing import *
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        # 字典直接相减
        # python min可加参数key
        return min((word for word in words if not cnt - Counter(word)), key=len)


licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
s = Solution().shortestCompletingWord(licensePlate,words)
print(s)