class Solution:
    def majorityElement(self, nums) -> int:
        # 在每一轮投票过程中，从数组中删除两个不同的元素，
        # 直到投票过程无法继续，此时数组为空或者数组中剩下的元素都相等。
        # 如果数组为空，则数组中不存在主要元素；
        # 如果数组中剩下的元素都相等，则数组中剩下的元素可能为主要元素。
        candidate = 'any'
        count = 0
        for each in nums:
            if count == 0:
                # 更新candidate，保证它是最有可能的主要元素
                candidate = each
            if each == candidate:
                count += 1
            else:
                count -= 1
        # 判断候选是否为主要元素
        if nums.count(candidate) >= len(nums)//2 + 1:
            return candidate
        return -1

# 请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

s = Solution().majorityElement([1,2,3,4,5,5,5,5,5])
print(s)