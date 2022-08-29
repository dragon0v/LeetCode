class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # 其它数+1，相当于这个数-1
        m = min(nums)
        return sum(e-m for e in nums)