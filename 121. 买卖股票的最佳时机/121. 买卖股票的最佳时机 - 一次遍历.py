class Solution:
    def maxProfit(self, prices):
        # 一次遍历，保存已经遍历部分的最低价格，每次将当前价格与最低价格相减得到可能的最大profit
        minprice = 1e9
        profit = 0
        for p in prices:
            profit = max(profit,p-minprice)
            minprice = min(p,minprice)
        return profit