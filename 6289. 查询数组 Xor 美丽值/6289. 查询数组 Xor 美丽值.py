class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # 花里胡哨的题干，瞎猜了一下然后用例都对，就提交了。。。
        return reduce(xor,nums)