class Solution:
    def minMoves(self, nums) -> int:
        # 其它数+1，相当于这个数-1
        # 之前还是想太复杂了，只要在一次遍历里把所有元素加起来，再减去最小值乘以个数即可
        # 不过有可能溢出
        min = nums[0]
        res = 0
        len = 0
        for n in nums:
            if min>n:
                min = n
            res += n
            len += 1
        return res-min*len

s = Solution()
t = s.minMoves([83,86,77,15,93,35,86,92,49,21])
print(t) # 487