from typing import *
from random import randrange
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        return ans


# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
# 水塘抽样，遍历nums，当我们第i次遇到值为target的元素时，
# 随机选择区间[0,i)内的一个整数，如果其等于 0，则将返回值置为该元素的下标，否则返回值不变。
# i=1时必为此下标，i=2时有1/2概率更新下标，同理易得每次的返回值是存在且概率平均的

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/random-pick-index/solution/sui-ji-shu-suo-yin-by-leetcode-solution-ofsq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)