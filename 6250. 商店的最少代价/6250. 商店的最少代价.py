class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # 有点前缀和的感觉，先计算在0时刻关门的cost，然后一次遍历求cost[i]
        c = Counter(customers)
        cost = c['Y']
        mincost = cost
        close = 0
        for i,d in enumerate(customers):
            if d=='Y':
                cost -= 1
            if d=='N':
                cost += 1
            if cost<mincost:
                mincost = cost
                close = i+1
        
        return close