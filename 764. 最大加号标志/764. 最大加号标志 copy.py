from typing import *
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 更超时
        mines = set(map(str,mines))  # 实验证明tuple最快
        res = 0
        # 枚举每个中心的位置
        for i in range(n):
            for j in range(n):
                if str([i,j]) not in mines:
                    for k in range(1,n//2+1):
                        if not all([i-k>=0, i+k<n, j-k>=0, j+k<n, 
                                "[%s,%s]"%(i-k,j) not in mines, "[%s,%s]"%(i+k,j) not in mines, 
                                "[%s,%s]"%(i,j-k) not in mines, "[%s,%s]"%(i,j+k) not in mines]):
                            k -= 1  # 失败了k-1
                            break
                    res = max(res,k+1)
        return res

s = Solution()
t = s.orderOfLargestPlusSign(500,[[4,2]])  # 34.411 seconds
print(t)