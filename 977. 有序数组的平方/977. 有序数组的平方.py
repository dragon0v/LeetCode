class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]**2]
        # 双指针，将ij放在数组中间
        for t in range(len(nums)-1):
            if nums[t+1] >= 0:
                i,j = t,t+1
                break
            if t == len(nums)-2:
                i,j = t,t+1
        # 然后ij往两边走，把小的平方数放res
        res = []
        while i>=0 and j <= len(nums)-1:
            t1=nums[i]**2
            t2=nums[j]**2
            if t1 < t2:
                res.append(t1)
                i -= 1
            else:
                res.append(t2)
                j += 1
        # 一边走到头了，再把剩下一边走完
        while i>=0:
            res.append(nums[i]**2)
            i -= 1
        while j <= len(nums)-1:
            res.append(nums[j]**2)
            j += 1



        return res