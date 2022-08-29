from typing import *
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 官方思路：
        # 结束时间早的一定先学
        courses.sort(key=lambda l:l[1])
        # 使用优先队列，将遇到的每一门课加入队列，
        # 直到总和超过目前的结束时间
        # 此时取出其中需要时间最长的课程，如果新来的课程比他短，则取代
        q = []
        total = 0

        for t,d in courses:
            if total + t <= d:
                total += t
                # python自带的是小根堆，所以把t取反传入，就成了大根堆
                heapq.heappush(q,-t)
            elif q and -q[0] > t:
                # q[0]是负数，t是正数
                total = total - (-q[0]) + t
                heapq.heappop(q)
                heapq.heappush(q,-t)
        return len(q)

# 抄题解的，作为heapq的学习，思路最重要，看着简单思路不好想
# 困难题但感觉中等左右

s = Solution()
t = s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
print(t)