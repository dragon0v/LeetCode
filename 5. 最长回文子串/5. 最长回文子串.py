class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = 1
        ans = s[0]
        tans = ''
        n = len(s)

        # 回文串奇数的情况
        for i in range(n):
            j = k = i
            tans = s[i]
            while j-1>=0 and k+1<n and s[j-1]==s[k+1]:
                tans = s[j-1] + tans + s[k+1]
                j -= 1
                k += 1
            if len(tans)>long:
                ans = tans
                long = len(tans)
        if len(tans)>long:
                ans = tans
                long = len(tans)
                
        # 回文串偶数的情况
        for i in range(n):
            j = i
            if i+1<n:
                k = i+1
            else:
                break
            tans = ''
            while j-1>=0 and k+1<n and s[j]==s[k]:
                tans = s[j] + tans + s[k]
                j -= 1
                k += 1
            if len(tans)>long:
                ans = tans
                long = len(tans)
        if len(tans)>long:
                ans = tans
                long = len(tans)
        
        return ans

# 写的很烂，又臭又长
# 执行用时：1276 ms


s = Solution()
t = s.longestPalindrome('a')
print(t)