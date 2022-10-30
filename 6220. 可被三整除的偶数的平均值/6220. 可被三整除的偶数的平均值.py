class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        t = 0
        for n in nums:
            if n%6==0:
                s += n
                t += 1

        return s//t if t>0 else 0