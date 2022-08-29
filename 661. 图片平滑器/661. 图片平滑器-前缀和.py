from typing import *
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        sum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + img[i - 1][j - 1]
        ans = [[0] * n for _ in range(m)]
        print(sum)
        for i in range(m):
            for j in range(n):
                a, b = max(0, i - 1), max(0, j - 1)
                c, d = min(m - 1, i + 1), min(n - 1, j + 1)
                cnt = (c - a + 1) * (d - b + 1)
                tot = sum[c + 1][d + 1] - sum[a][d + 1] - sum[c + 1][b] + sum[a][b]
                ans[i][j] = tot // cnt
        return ans

# 前缀和，presum为当前格和其左上角长方形中的元素和，
# presum(当前格) = presum(左格)+presum(上格)-presum(左上格角)+当前格值
# total(当前区域) = presum(右下角)-presum(左下角)-presum(右上角)+presum(左上角)

# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/image-smoother/solution/by-ac_oier-nn3v/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = Solution().imageSmoother([[1,100,1],[1,9999,1000]])
print(s)