from typing import *
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [None] * len(score)
        # dict 记录排序后的顺序，记录排序前顺序也可以做
        d = dict()
        ss = sorted(score,reverse=True)
        for i,v in enumerate(ss):
            d[v] = i+1 # d[score]=rank
        for i,v in enumerate(score):
            ranks[i] = str(d[v]) if d[v]>3 else ['Gold Medal','Silver Medal','Bronze Medal'][d[v]-1]
        return ranks
# nlogn
s = Solution()
t = s.findRelativeRanks([1,2,3,4,5,6,-1,-2])
print(t)