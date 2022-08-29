class Solution:
    def longestSubarray(self, nums, limit):
        i=j=0
        localmin = [100009,-1] # 数值和下标
        localmax = [-1,-1]
        res = 1
        
        for p,v in enumerate(nums):
            if v>localmax[0]:
                localmax = [v,p]
            elif v<localmin[0]:
                localmin = [v,p]
            if(localmax[0]-localmin[0] > limit):
                res = j-i
                i = min(localmax[1],localmin[1])
            j+=1
        
        return res

s = Solution()
print(s.longestSubarray([8,2,4,7],4))