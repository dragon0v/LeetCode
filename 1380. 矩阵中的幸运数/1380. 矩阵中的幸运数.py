class Solution:
    def luckyNumbers (self, matrix):
        res = []
        rowmin = [min(matrix[i]) for i in range(len(matrix))]
        colmax = []
        for j in range(len(matrix[0])):
            colmax.append(max([matrix[k][j] for k in range(len(matrix))]))
        
        print(rowmin,colmax)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == rowmin[i] and matrix[i][j] == colmax[j]:
                    res.append(matrix[i][j])
        
        return res

s = Solution()
t = s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
print(t)