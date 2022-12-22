from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # 几天后成每日一题了，发现sum里面不需要列表，sum可以对生成器使用
        # print(type(1 if '+' in op else -1 for op in operations))
        return sum(1 if '+' in op else -1 for op in operations)

s = Solution()
t = s.finalValueAfterOperations("--X")
print(t)