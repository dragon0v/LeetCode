class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<=1:
            return len(nums)
        i,j = 0,0
        while j<len(nums):
            if nums[j] == nums[i]:
                j+=1
            else:
                nums[i+1] = nums[j]
                i += 1

        return i+1

s = Solution()
t = s.removeDuplicates([1,1,1,1,1,1,2,3,4,5])
print(t)

# 这题要求原地算法，好像只能使用快慢指针
# TODO 为什么？