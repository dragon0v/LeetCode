class Solution:
    def find132pattern(self, nums) -> bool:
        stack = []
        k = -(10 ** 9 + 7)
        for i in range(len(nums) - 1,-1,-1):
            print(stack)
            if nums[i] < k:
                return True
            # 维护的递减栈，出现非递减的值弹栈直到重新递减
            while stack and stack[-1] < nums[i]:
                k = max(k,stack.pop())
            stack.append(nums[i])
        return False

s = Solution()
t = s.find132pattern([1,2,3,4,5,3,4,-1,0,1,3,4])
print(t)


# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/132-pattern/solution/xiang-xin-ke-xue-xi-lie-xiang-jie-wei-he-95gt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 单调栈
# 从后往前维护一个单调递减栈，同时用k记录所有出栈元素的最大值