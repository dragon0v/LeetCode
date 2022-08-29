class Solution:
    def thirdMax(self, nums):
        
        big1 = -1 * 1<<31
        big2 = -1 * 1<<31
        big3 = -1 * 1<<31

        # 保持big1最大，big2第二大，big3第三大
        for i in range(len(nums)):
            if nums[i] > big1:
                big3, big2, big1 = big2,big1,nums[i]
            elif nums[i]!=big1 and nums[i] > big2:
                big3, big2 = big2,nums[i]
            elif nums[i]!=big1 and nums[i]!=big2 and nums[i] > big3:
                big3 = nums[i]
            print(big1,big2,big3)

        return big3 if big3!=-1 * 1<<31 else big1

s = Solution()
t = s.thirdMax([2,2])
print(t)