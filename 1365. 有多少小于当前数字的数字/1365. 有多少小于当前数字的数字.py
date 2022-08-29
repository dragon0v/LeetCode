class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in range(len(nums)):
            n = nums[i]
            c = 0
            for num in nums:
                if(num < n):
                    c+=1
            ans.append(c)
        return ans
#最直白的方法，显然考点不在这
#->哈希表