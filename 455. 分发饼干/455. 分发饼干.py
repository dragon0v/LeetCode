class Solution:
    def findContentChildren(self, g, s) -> int:
        # 简单题，贪心，但其实很简单
        # 给剩余孩子里最小饥饿度的孩子分配最小的能饱腹的饼干
        res = 0
        g.sort()
        s.sort()
        for each in s:
            if res > len(g)-1:
                break
            if each>= g[res]:
                res += 1
        
        return res