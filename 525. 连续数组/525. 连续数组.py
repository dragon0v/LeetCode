class Solution:
    def findMaxLength(self, nums) -> int:
        from itertools import accumulate
        preSum = list(accumulate(nums))
        print(preSum)

        ans = -1

        for i,v in enumerate(preSum):
            if v*2 >= i:
                for j in range(i):
                    if v-preSum[j]==(i-j+1)/2:
                        ans = max(ans,i-j+1)

# TODO 
s = Solution()
t = s.findMaxLength([0,0,1,1,0,0,1])
print(t)