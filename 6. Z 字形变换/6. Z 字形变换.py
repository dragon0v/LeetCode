class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = [['' for _ in range(len(s))] for _ in range(numRows)]
        print(rows)
        i,j = 0, 0
        direction = 1 # 1表示向下，2表示向上
        for c in s:
            rows[i][j] = c
            if i+1 == numRows:
                direction = 2
            elif i == 0:
                direction = 1

            if direction==1:
                i += 1
            else:
                i -= 1
                j += 1
        res = ''
        for idx in range(numRows):
            res += ''.join(rows[idx])
        return res
                
# 模拟，7%，5%
s = Solution()
t = s.convert("fwkkowpdknedafmhcqzxpqrnyouuwlvbifnybcbnqisspezrwbqlrkbry",37)
print(t)