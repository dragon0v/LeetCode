class Solution:
    def removeElement(self, nums, val) -> int:
        i,j = 0,0
        while j<len(nums):
            print(i,j,nums[j])
            if nums[j]==val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        
        return i


s = Solution()
t = s.removeElement([1,2,3,4,4,4,3,2],4)
print(t)

# 类似26，快慢指针