from typing import *
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        t = 0
        for d in b:
            t = t*10 + d
        return pow(a,t,1337)
        # return pow(a, int("".join(map(str,b))), 1337)

s = Solution().superPow(3,[1,2,3,3])
print(s)