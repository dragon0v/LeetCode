class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 原数组arr=abcdef
        # 排序后=123456,
        # 则如果ab是一个块，则ab一定是1和2；如果def是一个块，则def一定是456
        # 由于数字取值是0~n-1，所以可以比较最大值
        return sum([max(arr[:i+1]) == i for i in range(len(arr))])