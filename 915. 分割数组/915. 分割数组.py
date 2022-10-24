class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lmax = -1
        rmin = min(nums)
        for i,v in enumerate(nums):
            lmax = max(lmax,v)
            if v==rmin:
                rmin = min(nums[i+1:])
            if lmax <= rmin:
                return i+1

# 1148 ms, 2022-02-08
