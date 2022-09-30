class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 第一次遍历找到有0的行列，用哈希表记录，再次遍历填充0
        if matrix==[]:
            return []
        zerosr = set()
        zerosc = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zerosr.add(r)
                    zerosc.add(c)
        # print(zeros)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zerosr or c in zerosc:
                    matrix[r][c] = 0