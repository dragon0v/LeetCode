class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # 中等，贪心
        # 这题开始有点贪心的感觉了
        # LeetCode101.pdf
        # 思路是尽可能保留区间结尾小且不相交的区间，这样可以保证尽可能保留多的元素个数
        
        if len(intervals)<=1:
            return 0
        res = 0

        # 首先将数组按结尾元素大小升序排序
        # sort的key参数指定比较的元素
        intervals.sort(key=lambda li:li[1])
        print(intervals)

        # 然后保留区间结尾小且不想交的区间
        # 当前的区间结尾
        prev = intervals[0][1]
        for each in intervals[1:]:
            # 重叠，所以移除，res+1
            if each[0] < prev:
                res += 1
            else:
                prev = each[1]
        return res

s = Solution()
t = s.eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]])
print(t)