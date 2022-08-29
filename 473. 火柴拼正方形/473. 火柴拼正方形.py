from typing import *
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        if n % 4 != 0:
            return False
        if max(matchsticks)>n//4:
            return False
        matchsticks.sort(reverse=True)

        # 回溯，只需要都放的进就行
        edges = [0] * 4
        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= n // 4 and dfs(idx + 1):  # 放的进，考虑下一个
                    return True
                edges[i] -= matchsticks[idx]  # 放不进，尝试下一个edge
            return False
        return dfs(0)




s = Solution()
t = s.makesquare([5,5,5,5,4,4,4,4,3,3,3,3])
print(t)