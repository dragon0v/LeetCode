class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def paint(r,c,p='-'):
            for i in range(len(matrix[0])):
                if matrix[r][i] != 0:
                    matrix[r][i] = p
            for j in range(len(matrix)):
                if matrix[j][c] != 0:
                    matrix[j][c] = p

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    paint(row,col,'-')
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '-':
                    matrix[row][col] = 0

# 不使用额外空间的原地算法
# 算是python特异解法，list可以有不同类型数据
# TODO研究其他解法