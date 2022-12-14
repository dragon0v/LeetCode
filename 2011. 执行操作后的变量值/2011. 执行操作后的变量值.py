from itertools import accumulate


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return list(accumulate([1 if '+' in op else -1 for op in operations]))[-1]
        # 不就是sum吗