class Solution:
    def jump(self, nums) -> int:
        # 贪心
        # 正向查找能到达的最远距离
        
        res = 0
        # t是长度，比下标大1
        t = len(nums)
        if t==1:
            return 0
        while t>1:
            for i in range(t):
                if i+nums[i] >= t-1:
                    t = i+1
                    res += 1
                    break
        
        return res

s = Solution().jump([1,1,1,1,1])
print(s)