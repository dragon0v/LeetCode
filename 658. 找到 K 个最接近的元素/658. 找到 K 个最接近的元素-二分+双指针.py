from typing import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 思路：二分查找+双指针
        i,j = 0,len(arr)-1
        while i<=j:
            t = (i+j)/2
            if arr[t]==k:
                break
            if arr[t]>k:
                j = t-1
            else:
                i = k+1
         
            

s = Solution()
t = s.findClosestElements([1,2,3,4,5,6],3,3)
print(t)