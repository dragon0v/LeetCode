class NumMatrix:

    def __init__(self, matrix):
        self.presum = []
        for row in matrix:
            t = [0]
            for each in row:
                t.append(t[-1]+each)
            self.presum.append(t)
        print(self.presum)
        assert len(self.presum)==len(matrix) and len(self.presum[0])==len(matrix[0])+1

    def sumRegion(self, row1, col1, row2, col2):
        sum = 0
        for row in range(row1,row2+1):
            sum+=self.presum[row][col2+1]-self.presum[row][col1]
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 思路：参考303，计算矩阵的前缀和，矩阵每行计算前缀和
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
nm = NumMatrix(matrix)
print(nm.sumRegion(1,2,3,4))