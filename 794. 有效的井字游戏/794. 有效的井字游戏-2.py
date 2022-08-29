class Solution:
    def validTicTacToe(self, board) -> bool:
        # 不通过的
        # 判断个数
        s = board[0]+board[1]+board[2]
        a = ''
        if not (s.count('X') == s.count('O') or s.count('X')-1 == s.count('O')):
            print(1)
            return False
        # 判断胜利，前提是格子还没被铺满
        # 情况1 X或O连成3个，此时另一方必须不能连成三个
        if s[0]==s[3]==s[6]=='X' or s[0]==s[1]==s[2]=='O' or s[1]==s[4]==s[7]=='X' or s[1]==s[4]==s[7]=='O' \
            or s[2]==s[5]==s[8]=='X' or s[2]==s[5]==s[8]=='O'


s = Solution()
t = s.validTicTacToe(["XXX","XOO","OO "]  )
print(t)

# 没这么简单，["OXX","XOX","OXO"]