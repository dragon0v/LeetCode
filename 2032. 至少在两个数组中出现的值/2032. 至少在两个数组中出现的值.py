class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # 用sum + in，自我感觉还是蛮巧妙的
        res = []
        for i in range(1,101):
            if sum([i in nums1, i in nums2, i in nums3]) >= 2:
                res.append(i)
        return res
