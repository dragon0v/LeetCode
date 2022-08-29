class Solution:
    def arrangeCoins(self, n: int) -> int:
        i,j = 0,n
        while i<j:
            print(i,j)
            k = (i+j+1)//2
            if k*(k+1) > 2*n:
                j = k-1
            else:
                i = k
            
        return i
            

# 二分查找
s = Solution()
t = s.arrangeCoins(1212)
print(t)