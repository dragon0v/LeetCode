class Solution:
    def maxProfit(self, prices):
        profit = 0
        localmaxindex = -1
        
        for i,p in enumerate(prices):
            if(i>=localmaxindex):
                localmaxvalue = 0
                for j,v in enumerate(prices[i+1:]):
                    if(v >= localmaxvalue):
                        localmaxindex = j # 这样更新到的下标是最靠右的
                        localmaxvalue = v
            profit = max(profit,localmaxvalue-p)
            
        return profit
#仍然超时