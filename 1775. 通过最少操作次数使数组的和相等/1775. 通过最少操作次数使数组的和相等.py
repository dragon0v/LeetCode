class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # 判断是否能成功
        l1, l2 = len(nums1),len(nums2)
        if min(l1,l2)*6<max(l1,l2):
            return -1

        if sum(nums1)==sum(nums2):
            return 0
        # 保证nums1是和较小的那个
        if sum(nums1)>sum(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        nums2.sort()

        # 贪心：每次将较大数组中的最大值改成1，较小数组的最小值改成6
        # 双指针
        i = 0
        j = len(nums2)-1
        diff = abs(sum(nums1)-sum(nums2))
        res = 0
        while diff>0:
            res += 1
            if 7-nums1[i] > nums2[j]:
                diff -= 6-nums1[i]
                i += 1
            else:
                diff -= nums2[j]-1
                j -= 1

        return res
        