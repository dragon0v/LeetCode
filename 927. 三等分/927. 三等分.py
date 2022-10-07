from typing import *
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # 超时，108 / 121 个通过测试用例
        def cal2(s):
            res = 0
            for c in s:
                res = res*2 + c
            return res
        i,j = 0,0  # return [i,j], 每次控制i，获得第1个数；变j，当1=2=3时return，第2个数超过第1个数时，i++
        n = len(arr)
        for i in range(n-1):
            crt = cal2(arr[:i])
            for j in range(i+1,n):
                crt2 = cal2(arr[i:j])
                if crt2==crt:
                    if cal2(arr[j:])==crt:
                        return [i-1,j] if i>0 else [i,j+1]
                    else:
                        break
                elif crt2>crt:
                    break
        
        return [-1,-1]


s = Solution()
t = s.threeEqualParts([1,1,0,0,1])
print(t)