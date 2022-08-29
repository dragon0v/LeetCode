class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # 先扫一遍获得0的位置
        zeros = []
        for i,c in enumerate(arr):
            if c==0:
                zeros.append(i)
        