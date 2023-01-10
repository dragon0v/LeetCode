class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 模拟，数据不大就硬编码了
        check = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        board = ['' for i in range(9)]
        for i,m in enumerate(moves):
            board[m[0]*3+m[1]] = 'B' if i%2 else 'A'
            for c in check:
                # python连等真的方便
                if board[c[0]]==board[c[1]]==board[c[2]] and board[c[0]]!='':
                    return board[c[0]]
        
        if len(moves)!=9:
            return 'Pending'
        return 'Draw'