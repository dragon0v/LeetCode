class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k %= n
        print(id(nums))
        for _ in range(k):
            nums.insert(0, nums.pop()) # 默认pop的是最后的元素，插入到最前面
        print(id(nums),nums)

s = Solution()
t = s.rotate([1,2,3,4,5,6,7],3)
print(t)


# 作者：wu_yan_zu
# 链接：https://leetcode-cn.com/problems/rotate-array/solution/san-ci-fan-zhuan-fu-yi-xie-pythonicde-jie-fa-pytho/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 这个也是空间O1的