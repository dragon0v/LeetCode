class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # åįžå
        presum = [0]
        for g in gain:
            presum.append(presum[-1]+g)
        return max(presum)