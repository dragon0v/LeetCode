from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a: int, b: int) -> int:
            return a if b==0 else gcd(b,a%b)
        c = Counter(deck)
        l = c.values()
        return reduce(gcd,l)>=2