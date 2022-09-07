import heapq
from typing import List
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # 贪心+优先队列：优先吃保质期快到的
        # 参考了 https://leetcode.cn/problems/maximum-number-of-eaten-apples/solution/1705-chi-ping-guo-de-zui-da-shu-mu-pytho-4e77/
        pq = []
        ans = 0

        # 边摘边吃
        for i,(a,d) in enumerate(zip(apples,days)):
            # 摘苹果
            if a!=0:
                heapq.heappush(pq,[i+d,a])  # 过期日,数量
            
            # 丢掉已过期的苹果，保证小根堆中最小的苹果未过期
            while pq and pq[0][0] < i+1:  
                heapq.heappop(pq)
            
            # 吃一个苹果
            if pq:
                pq[0][1] -= 1
                ans += 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)
        
        # 没苹果摘了，吃剩下的
        i += 1
        while pq:
            # 扔
            while pq and pq[0][0] < i+1:  
                heapq.heappop(pq)
            
            # 吃一个苹果
            if pq:
                pq[0][1] -= 1
                ans += 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)

            # 下一天
            i += 1
        
        return ans
                    
            

s = Solution()
apples = [2,1,0,0,0,0,0,1,1]
days = [1000,1000,0,0,0,0,0,1,1]  # 第三天开始吃不到，答案是4
t = s.eatenApples(apples,days)
print(t)