class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        n = len(prices)
        for i,p in enumerate(prices):
            sub = 0  # 不需要flag
            for j in range(i+1,n):
                if prices[j]<=p:
                    sub = prices[j]
                    break
            ans.append(p-sub)
        
        return ans