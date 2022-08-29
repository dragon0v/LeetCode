class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        appeared = [0 for _ in range(n)]
        res = []
        for num in nums:
            appeared[num-1] += 1
        for i,v in enumerate(appeared):
            if v==0:
                res.append(i+1)
        return res
        