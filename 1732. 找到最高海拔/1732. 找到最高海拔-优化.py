class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 前缀和，无需数组，只需保留最大值和当前前缀和即可
        res, presum = 0,0
        for g in gain:
            presum += g
            res = max(res,presum)
        return res