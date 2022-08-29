class NumArray:

    def __init__(self, nums):
        self.presum = [0]
        for n in nums:
            self.presum.append(self.presum[-1]+n)

    def sumRange(self, i: int, j: int) -> int:
        return self.presum[j+1] - self.presum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 思路：构建前缀和，presum[i] = sum[:i] = presum[i-1] + nums[i-1]
# sum(nums[i:j+1]) = presum[j+1]-presum[i]

# _sum 可以替代self.sum -- 为什么？
'''
_var ；变量名前一个下划线来定义，此变量为保护成员protected，只有类及其子类可以访问。此变量不能通过from XXX import xxx 导入
__var;变量名前两个下划线来定义，此变量为私有private，只允许类本身访问，连子类都不可以访问。
'''
r = NumArray([1,2,3])
print(r.sumRange(1,2))