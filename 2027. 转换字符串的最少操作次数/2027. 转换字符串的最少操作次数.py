class Solution:
    def minimumMoves(self, s: str) -> int:
        # 贪心：出现x就把它和此后2个置为0，永远是最优解
        res = 0
        i = 0
        while i<len(s):
            if s[i]=='X':
                res += 1
                i += 3
            else:
                i += 1
        return res