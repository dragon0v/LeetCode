from typing import *
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [1 for _ in score]
        for s in score:
            for i in range(len(score)):
                if s>score[i]:
                    ranks[i] += 1
        for i in range(len(ranks)):
            if ranks[i] == 1:
                ranks[i] = 'Gold Medal'
            elif ranks[i] == 2:
                ranks[i] = 'Silver Medal'
            elif ranks[i] == 3:
                ranks[i] = 'Bronze Medal'
            else:
                ranks[i] = str(ranks[i])
        return ranks
# 复杂度n^2
s = Solution()
t = s.findRelativeRanks([1,2,3,4,5,6])
print(t)