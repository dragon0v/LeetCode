class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1的大小为m+n
        """
        if m==0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        # 从后看，把较大的放进去
        i,j = m-1, n-1
        k = m+n-1 # 当前插入的位置
        while j >= 0 and i >= 0:
            # 101pdf里的cpp解法很精简
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        while j >=0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return nums1

s = Solution()
t = s.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(t)
t = s.merge([0,0,0],0,[2,5,6],3)
print(t)
t = s.merge([],0,[],0)
print(t)
t = s.merge([1],1,[],0)
print(t)