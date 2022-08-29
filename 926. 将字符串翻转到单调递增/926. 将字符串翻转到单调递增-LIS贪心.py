class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 令s长度为n，原问题等价于在 s 中找到最长不下降子序列，设其长度为ans，那么对应的n−ans即是答案。
        # LIS为一类模板
        n = len(s)
        ans = 0
        g = [n+10]*(n+10)
        for i in range(n):
            t = int(s[i])
            l,r = 1,i+1
            while l<r:
                mid = (l+r)//2
                if g[mid]>t:
                    r = mid
                else:
                    l = mid + 1 
            g[r] = t
            ans = max(ans,r)
        
        return n-ans
