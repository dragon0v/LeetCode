from typing import *
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def haszero(x):
            return '0' in str(x)
        for i in range(1,n):
            if not haszero(i) and not haszero(n-i):
                return [i,n-i]