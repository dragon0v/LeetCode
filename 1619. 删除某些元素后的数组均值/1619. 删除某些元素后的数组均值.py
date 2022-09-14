from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # arr.length 是 20 的 倍数 
        return sum(sorted(arr)[int(0.05*len(arr)):int(0.95*len(arr))]) / (0.9*len(arr))
        # 更优雅一些
        return sum(sorted(arr)[len(arr)//20:-len(arr)//20]) / (0.9*len(arr))