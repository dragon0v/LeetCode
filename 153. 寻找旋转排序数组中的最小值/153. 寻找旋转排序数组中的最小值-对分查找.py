class Solution:
    def findMin(self, nums) -> int:
        i = 0
        j = len(nums)-1
        while i<=j:
            k = (i+j)//2
            if nums[k-1]>nums[k]:
                return nums[k]
            if nums[i] < nums[k]:
                i = k+1
            elif nums[k] < nums[j]:
                j = k-1
        return nums[0]
                
                
s = Solution().findMin([2,1])
print(s)


# 这题是中等题，就应该想一个Ologn的解法
# 对分查找
# 力扣官方题解的画图法很好，有助于思考
# 要找的target一定是最小值，特点是其左边的值大于它

