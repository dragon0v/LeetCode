from typing import *
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 思路：统计每个年龄的人数，获得前缀和，然后找边界
        a = [0] * 121
        for age in ages:
            a[age]+=1
        pre = [0]
        for i in a:
            pre.append(pre[-1]+i)
        print(pre)
        
        ans = 0
        for i in range(15,121):
            if a[i]>0:
                bound = int(i*0.5+8)
                ans += a[i] * (pre[i]-pre[bound-1]-1)
        return ans

s = Solution()
t = s.numFriendRequests([16,16])
print(t)