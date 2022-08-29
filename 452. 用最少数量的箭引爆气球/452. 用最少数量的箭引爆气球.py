class Solution:
    def findMinArrowShots(self, points) -> int:
        # 中等，贪心
        # 思路和435类似，按右边界排序，然后按右边界射箭
        cnt = 1
        points.sort(key=lambda li:li[1])
        # 第一支箭射在右边界
        arrow = points[0][1]
        for ballon in points:
            # 射不破了
            if ballon[0] > arrow:
                cnt += 1
                arrow = ballon[1]
            # else这个ballon被射破，什么也不做

        return cnt

