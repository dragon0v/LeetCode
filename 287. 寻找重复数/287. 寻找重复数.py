class Solution:
    def findDuplicate(self, nums):
        # 维持nums前i个数有序
        for i in range(1,len(nums)):
            
