class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        li=nums1+nums2
        li.sort()
        l = m+n
        if l%2 == 1:
            return li[l//2]
        return (li[l//2]+li[l//2-1])/2






# 属于犯规的解法，不认为做出了

# [1,2,3],[4,5,6]
# [1,3],[2]
# [4,5,6],[1,2]


s = Solution()
t = s.findMedianSortedArrays([1,2,3],[4,5,6])
print(t)
# 进阶：你能设计一个时间复杂度为 O(log l) 的算法解决此问题吗？