from typing import *
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 超时
        res = 0
        # 枚举每个中心的位置
        for i in range(n):
            for j in range(n):
                if [i,j] not in mines:
                    for k in range(1,n//2+1):
                        if not all([i-k>=0, i+k<n, j-k>=0, j+k<n, 
                                [i-k,j] not in mines, [i+k,j] not in mines, 
                                [i,j-k] not in mines, [i,j+k] not in mines]):
                            k -= 1  # 失败了k-1
                            break
                    res = max(res,k+1)
        return res

s = Solution()
t = s.orderOfLargestPlusSign(500,[[4,2]])  # 14.882 seconds
print(t)