from typing import *
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def average(r,c):
            sum = cnt = 0
            for i in range(max(0,r-1),min(n,r+2)):
                for j in range(max(0,c-1),min(m,c+2)):
                    sum += img[i][j]
                    cnt += 1
            return sum//cnt
        
        m,n = len(img[0]), len(img)
        res = [[0 for _ in range(m)] for _ in range(n)]
        # print(res)
        for col in range(m):
            for row in range(n):
                res[row][col] = average(row,col)
        return res
# 时间复杂度：O(m∗n∗C)，其中 C 为灰度单位所包含的单元格数量，固定为 9
# 空间复杂度：O(m∗n)

s = Solution().imageSmoother([[1,100,1],[1,0,100]])
print(s)