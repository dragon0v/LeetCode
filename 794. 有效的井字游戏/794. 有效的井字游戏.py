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
        if ' ' in s:
            for r in range(3):
                if s[r*3:r*3+3] == 'OOO' or s[r*3:r*3+3] == 'XXX':
                    print(2)
                    return False
                if s[r] == s[3+r] == s[6+r] == 'X' or s[r] == s[3+r] == s[6+r] == 'O':
                    print(3)
                    return False
            if s[0] == s[4] == s[8] == 'X' or s[0] == s[4] == s[8] == 'O':
                print(4)
                return False
            if s[2] == s[4] == s[6] == 'X' or s[2] == s[4] == s[6] == 'O':
                print(5)
                return False
        return True


s = Solution()
t = s.validTicTacToe(["XXX","XOO","OO "]  )
print(t)

# 没这么简单，["OXX","XOX","OXO"]