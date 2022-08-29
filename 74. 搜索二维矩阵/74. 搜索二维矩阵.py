class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 这里用顺序，改进方法是对分
        for r in range(len(matrix)):
            print(r)
            if matrix[r][0]<=target and r+1 < len(matrix) and matrix[r+1][0]>target:
                return target in matrix[r]
        return target in matrix[-1]

s = Solution()
t = s.searchMatrix([[1],[3],[5]],3)
print(t)