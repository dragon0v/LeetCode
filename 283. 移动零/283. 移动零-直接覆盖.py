class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1)
        # 因为知道是0了，所以直接覆盖，后面补0
        i=0
        for each in nums:
            if each != 0:
                nums[i] = each
                i+=1
        for j in range(len(nums)-i):
            nums[i+j] = 0

a = [1,2,3,4,0,3,2,1,0,0,0]
s = Solution()
t = s.moveZeroes(a)
print(a)

