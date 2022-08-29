class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i,p in enumerate(prices):
            if(i!=len(prices)-1 and prices[i+1]>p):
                profit += prices[i+1]-p
        return profit
#思路：对每个上坡求和即可，如果第二天涨了就卖