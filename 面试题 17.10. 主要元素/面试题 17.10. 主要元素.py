class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = (len(nums)//2+1)
        nums.sort()
        last = 'a'
        l = 0
        for i in range(len(nums)):
            if nums[i]==last:
                l += 1
                if l >= target:
                    return nums[i]
            else:
                last = nums[i]
                l = 1
                if l>= target:
                    return nums[i]
        return -1

# 请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

# 不满足要求的