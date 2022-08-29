class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0 for _ in range(101)]
        ans = []
        for each in nums:
            count[each] += 1
        for i in range(100):
            count[i+1] += count[i]
        for each in nums:
            if(each!=0):
                ans.append(0)
            else:
                ans.append(count[each-1])
                
        return ans
