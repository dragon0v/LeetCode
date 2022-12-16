class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # 简单题
        t = sum(nums)
        goal = goal-t
        d,r = divmod(abs(goal),limit)
        return d if r==0 else d+1