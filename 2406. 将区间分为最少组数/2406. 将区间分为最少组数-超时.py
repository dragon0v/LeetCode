import typing


from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # 朴素解法，超时
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        ans = 0
        while len(intervals)>0:
            last = -10000000
            ans += 1
            i = 0
            while i<len(intervals):
                # print(i)
                n = intervals[i]
                if n[0]>last:
                    last = n[1]
                    intervals.pop(i)
                    i -= 1
                    # print(n[0],last,1)
                i += 1
        
        return ans