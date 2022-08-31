class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        n = len(prices)
        for i,p in enumerate(prices):
            f=True
            for j in range(i+1,n):
                if prices[j]<=p:
                    ans.append(p-prices[j])
                    f = False
                    break
            if f:
                ans.append(p)
        
        return ans