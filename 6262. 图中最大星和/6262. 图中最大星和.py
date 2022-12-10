class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # 错误两次，有一次写成c[:-k]，不应该
        n = len(vals)
        connected = [[] for _ in range(n)]
        for a,b in edges:
            connected[a].append(vals[b])
            connected[b].append(vals[a])
        for c in connected:
            c.sort()
        
        m = -1111111111
        for i,c in enumerate(connected):
            t = sum(x if x>0 else 0 for x in c[-k:]) + vals[i]
            m = max(m,t)
            
            # print(c[-k:])
            # print(t,c)
        
        return m