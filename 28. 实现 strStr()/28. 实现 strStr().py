class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if(n==0):
            return 0
        m = len(haystack)
        if(n>m):
            return -1
        for i,v in enumerate(haystack):
            for j in range(n):
                if(i+n-1 >= m or haystack[i+j]!=needle[j]):
                    break
                if(j==n-1):
                    return i
        return -1

# 与官方解法1类似