from typing import *
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 思路：条件3是条件2的子集，所以只考虑条件12即可
        # 条件1仅当y<=14成立
        # 所以先排序ages，对于每个age，找到一段范围
        l = 0 # 
        r = 0 # 算法会保证age在[l:r+1]的区间内
        res = 0
        n = len(ages)
        ages.sort()
        for age in ages:
            if age<15:
                continue
            while ages[l]<=0.5*age+7:
                l += 1
            while r+1<n and ages[r+1]<=age:
                r += 1
            res += r-l-1
        return res

s = Solution()
t = s.numFriendRequests([16,16])
print(t)