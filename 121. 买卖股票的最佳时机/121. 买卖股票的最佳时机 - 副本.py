

#思路：找历史最低点，然后在此后最高点卖出

class Solution:
    def maxProfit(self, prices):
        minprice = 1e9
        profit = 0
        for p in prices:
            profit = max(profit,p-minprice)
            minprice = min(p,minprice)
        