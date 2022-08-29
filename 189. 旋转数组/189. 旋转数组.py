class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k = k%n
        print(id(nums))
        
        nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]
        # 等同于以下：
        # k = k%n
        # nums[:] = nums[-k:] + nums[:-k]
        # 原地修改只有上面这种才行
        print(id(nums))

        # 不是原地修改，赋值操作对nums重新分配了地址，导致在力扣上无法通过
        nums = nums[len(nums)-k:]+nums[:len(nums)-k]
        print(id(nums))
        
        

s = Solution()
t = s.rotate([1,2,3,4,5,6,7],3)
print(t)

# 这题目的在于探索多种解法
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？ 
# --O(1)空间只有三次反转