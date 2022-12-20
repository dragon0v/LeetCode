class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 看了眼题解，二分很巧妙
        # 思路：二分假设结果是k，那么每个大于k的袋子最终分成n//k个，需要(n-1)//k次op
        i,j = 1,max(nums)
        res = 10**9+1
        while i<=j:
            k = (i+j)//2
            if sum([(n-1)//k for n in nums])<=maxOperations:  # 
                print(k)
                res = min(res,k)
                j = k-1
            else:
                i = k+1
        return res