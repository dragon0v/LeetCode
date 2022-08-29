class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs.sort()
        res = 0
        while coins>0 and len(costs)>0:
            coins -= costs.pop(0)
            if coins>=0:
                res += 1
        return res
    
# 一分钟的题，关键是看sorted用法