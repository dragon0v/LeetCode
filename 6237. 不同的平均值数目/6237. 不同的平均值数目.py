class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # 一开始走歪了硬模拟了，只要sort一下就可以不需要删除
        t = set()
        nums.sort()
        for i in range(len(nums)//2):
            t.add((nums[i]+nums[len(nums)-1-i])/2)
        return len(t)