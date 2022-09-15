from collections import deque
from typing import *
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 感觉是某种计数原理
        # 预处理arr[i]为最小值的最左端l和最右端r，其对res的贡献为 arr[i]*(i-l)*(r-i)
        # 由于存在重复值，取lr的时候一开一闭，可以避免重复计算
        MOD = 1e9+7
        # 使用单调栈进行预处理
        n = len(arr)
        l = [-1] * n
        r = [n] * n
        dq = []  # 单调栈
        # 往后看，直到arr[r]比arr[i]小
        for i in range(n):
            while dq and arr[dq[-1]]>=arr[i]:
                r[dq.pop()] = i  # 
            dq.append(i)
        dq = []
        for i in range(n-1,-1,-1):
            while dq and arr[dq[-1]]>arr[i]:
                l[dq.pop()] = i
            dq.append(i)
        
        res = 0
        for i in range(n):
            a = l[i]
            b = r[i]
            res += ((((i-a)*(b-i)) % MOD) * arr[i]) % MOD
        
        return int(res % MOD)

s = Solution()
t = s.sumSubarrayMins([1,2,3,4,5])
print(t)