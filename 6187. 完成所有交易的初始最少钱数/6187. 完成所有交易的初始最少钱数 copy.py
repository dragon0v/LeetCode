from typing import *
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # 1. 优先进行亏钱的交易
        # 2. 对每笔亏钱的交易，ans+=亏钱的数量
        # 3. 对赚钱的交易，ans+=最大的启动资金
        # 4. 若赚钱项目最大的启动资金少于亏钱项目最大的回报，则需要加上最大亏钱回报
        losses = 0
        maxlossback = 0
        maxprofitcost = 0
        for t in transactions:
            if t[0]-t[1] > 0:
                losses += t[0]-t[1]
                maxlossback = max(maxlossback,t[1])
            else:
                maxprofitcost = max(maxprofitcost,t[0])
        
        print(losses,maxlossback,maxprofitcost)
        return losses + maxprofitcost + max(0,maxlossback-maxprofitcost)
        

s = Solution()
tt = [[2,1],[5,0],[4,2]]  # 10，亏钱共8，最大亏钱回报2，无赚钱项目
tt = [[3,0],[0,3]]
tt = [[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]]  # 18
tt = [[7,2],[5,0],[4,1],[5,8],[5,9]]  # 18，亏钱共13，最大亏钱回报2，赚钱项目最大启动资金5，5>2，无需另准备
t = s.minimumMoney(tt)
print(t)