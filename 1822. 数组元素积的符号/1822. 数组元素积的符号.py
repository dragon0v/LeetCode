class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def sign(n):
            if n==0:
                return 0
            elif n>0:
                return 1
            return -1
        res = 1
        for n in nums:
            res *= sign(n)
        return res