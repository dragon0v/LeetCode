class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 没有要求空间复杂度O(1)，但是讲道理in-place就是要O(1)
        # 按顺序储存非0元素，修改，最后补0
        t=[]
        for each in nums:
            if each != 0:
                t.append(each)
        
        for i in range(len(t)):
            nums[i] = t[i]
        for i in range(len(t),len(nums)):
            nums[i] = 0
            
        





