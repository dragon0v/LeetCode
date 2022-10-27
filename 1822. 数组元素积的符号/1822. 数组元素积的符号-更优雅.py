class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            # 0直接返回
            if n==0:
                return 0
            # 正数不改变符号，没必要处理
            if n<0:
                res = -res
        return res