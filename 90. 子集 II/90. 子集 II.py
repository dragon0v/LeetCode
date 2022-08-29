class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for new in nums:
            res += [(old for old in res) + [new]]
        print(res)
        return list(set(res))