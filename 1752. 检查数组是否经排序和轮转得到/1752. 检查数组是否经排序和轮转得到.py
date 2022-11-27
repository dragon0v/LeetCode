class Solution:
    def check(self, nums: List[int]) -> bool:
        # 最多一个下降
        down = 0
        for i in range(n:=len(nums)):
            if nums[i]>nums[(i+1)%n]:
                down+=1
        return down<2