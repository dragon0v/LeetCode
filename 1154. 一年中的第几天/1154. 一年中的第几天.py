class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int,date.split('-'))
        mm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y != 1900 and y % 4 ==0:
            mm[2] += 1
        return sum(mm[: m]) + d
        # https://leetcode-cn.com/problems/day-of-the-year/comments/129055