class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        nums2 = nums[:]
        nums2.sort()
        for each in nums:
            ans.append(nums2.index(each))

        return ans
# 执行用时：60 ms, 在所有 Python3 提交中击败了55.38%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了21.86%的用户