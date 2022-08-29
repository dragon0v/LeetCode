from typing import *
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 1<=len(quiet)<=500
        # 0 <= richer.length <= n * (n - 1) / 2
        # 构造有向无环图，方向为更有钱的方向
        n = len(quiet)
        g = [[] for _ in range(n)] # g[i]中的元素一定比i更有钱
        for r in richer:
            g[r[1]].append(r[0])
        
        # dfs搜索每个比当前i更有钱的元素，找到最安静的，每次dfs完会保证ans[x]不为-1
        ans = [-1] * n
        def dfs(x):
            if ans[x] != -1:
                return
            ans[x] = x # 没有比x更有钱的就是x自己
            for y in g[x]: # 在比x更有钱的人里继续dfs，dfs后
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]
        
        for i in range(n):
            dfs(i)
        
        return ans

s = Solution().loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0])
print(s)