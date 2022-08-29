from typing import *
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean*(len(rolls)+n)
        c = (s-sum(rolls)) % n
        d = (s-sum(rolls)-c)//n
        if (c+d) > 6 or (c+d) < 1:
            return []
        if d > 6 or d < 1:
            return []
        return [c+d] + [d] * (n-1)
        # 不对的
s = Solution()
t = s.missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5],4,40)
print(t)