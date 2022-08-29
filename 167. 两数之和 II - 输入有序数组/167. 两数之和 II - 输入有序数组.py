class Solution:
    def twoSum(self, nums, target: int):
        # 双指针
        i,j = 0,len(nums)-1
        while i<j:
            if nums[i] + nums[j] == target:
                return [i+1,j+1]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        