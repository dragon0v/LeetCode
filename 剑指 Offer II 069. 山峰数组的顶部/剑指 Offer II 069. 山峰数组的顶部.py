class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
    
    # 最直接的想法，遍历找到极大值，O(n)