class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        i,j = 1, len(arr)-2
        while i<=j:
            k = (i+j)//2
            if arr[k] > arr[k-1] and arr[k] > arr[k+1]:
                return k
            elif arr[k] > arr[k-1] and arr[k] < arr[k+1]:
                i = k + 1
            else:
                j = k - 1
        
        return -1
    
    # 类似对分查找，找到极大值，O(logn)

s = Solution()
t = s.peakIndexInMountainArray([1,2,3,4,5,6,4,3,2])
print(t)