class Solution:
    def maxProfit(self, prices):
        # 两次遍历，是一次遍历的反思路
        # 第一次预处理i之后的最大值
        # 第二次将i后的最大值和p[i]相减得到可能的最大profit
        maxp = list(accumulate(prices[::-1],max))[::-1]
        print(maxp)
        profit = 0
        for i,p in enumerate(prices):
            profit = max(profit,maxp[i]-p)
        return profit