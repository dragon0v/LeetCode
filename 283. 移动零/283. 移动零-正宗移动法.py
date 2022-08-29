class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1)
        # 双指针，维护数组下标i前为非0的有序结果
        i,j = 0,0
        while j<len(nums) :
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1 # 由if-else简化得来，else的操作为j+=1，所以无论如何j都要—++




a = [1,2,3,4,0,3,2,1,0,0,0]
s = Solution()
t = s.moveZeroes(a)
print(a)

