class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board[0]), len(board)
        def adjacent(i,j):
            ret = []
            if i==0 and j==0:
                ret.append(board[i+1][j])
            
            
            