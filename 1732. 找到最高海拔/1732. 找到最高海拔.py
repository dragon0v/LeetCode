class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 前缀和
        presum = [0]
        for g in gain:
            presum.append(presum[-1]+g)
        return max(presum)