from typing import *
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 有的钱数x需大于所有亏钱项目（-a）
        # x-a需大于max(costs)，其中costs为不亏钱的项目的付费
        # 错误的思路
        losses = 0
        profitable = []
        maxdiff = 0
        for t in transactions:
            if t[0]-t[1] > 0:
                maxdiff = max(maxdiff,t[1])
                losses += t[0]-t[1]
            else:
                profitable.append(t)
        
        if profitable:
            return losses + sorted(profitable, key=lambda x:x[0])[-1][0]+maxdiff
        
        return losses+maxdiff

s = Solution()
tt = [[2,1],[5,0],[4,2]]
tt = [[3,0],[0,3]]
tt = [[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]  # 18
t = s.minimumMoney(tt)
print(t)