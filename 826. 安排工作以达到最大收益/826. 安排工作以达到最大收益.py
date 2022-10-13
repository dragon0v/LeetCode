class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 贪心，尽可能完成收益大的，且不存在任何竞争的情况
        works = sorted(zip(difficulty,profit))  # 根据难度排序
        ans = i = 0
        best = 0  # 储存了难度小于当前难度的最大利润
        worker.sort()  # 能力升序，和工作根据难度升序对应
        for ability in worker:
            while i<len(works) and ability >= works[i][0]:
                best = max(best,works[i][1])
                i += 1
            ans += best
        
        return ans