from itertools import zip_longest


class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        # zip_longest
        res = []
        for c1,c2 in zip_longest(w1,w2,fillvalue=''):
            # fillvalue默认为none
            res += [c1,c2]
        return ''.join(res)
