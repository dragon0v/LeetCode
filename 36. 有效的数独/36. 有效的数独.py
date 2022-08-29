class Solution:
    def isValidSudoku(self, board) -> bool:
        def hasDuplicate(nums):
            exist = []
            for n in nums:
                if n!= '.' and n in exist:
                    print(nums,n)
                    return True
                else:
                    exist.append(n)
            return False
        
        for row in board:
            if hasDuplicate(row):
                return False
        
        for col in range(9):
            if hasDuplicate([board[i][col] for i in range(9)]):
                return False


        for i in range(3):
            for j in range(3):
                if hasDuplicate(board[3*i][3*j:3*(j+1)]+board[3*i+1][3*j:3*(j+1)]+board[3*i+2][3*j:3*(j+1)]):
                    return False
        
        return True
    
c = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s = Solution().isValidSudoku(c)
print(s)

# 时间复杂度：读取三次矩阵
# TODO 看看别人是咋写的