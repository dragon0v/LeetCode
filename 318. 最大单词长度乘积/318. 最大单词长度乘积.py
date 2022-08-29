from typing import *
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda n:len(n),reverse=True)
        # print(words)
        maxlen = 0
        for one in words:
            pass

s = Solution().maxProduct(["asds","sadasdad","sda"])
print(s)