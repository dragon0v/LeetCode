class Solution:
    def minMoves(self, nums) -> int:
        # 其它数+1，相当于这个数-1
        count = 0
        res = 0
        min = nums[0]
        for n in nums:
            if min > n:
                res += count * (min-n)
                min = n
            else:
                res += n - min
            count += 1
        
        return res

s = Solution()
t = s.minMoves([83,86,77,15,93,35,86,92,49,21])
print(t) # 487