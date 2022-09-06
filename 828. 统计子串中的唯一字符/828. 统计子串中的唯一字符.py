from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 思路：预处理出两数组 l 和 r 分别代表 s[i] 作为子数组唯一字符时，其所能到达的最远两端：
        n = len(s)
        l = []
        r = []
        idx = [-1] * 26
        for i in range(n):
            ch = ord(s[i]) - ord('A')
            l.append(idx[ch])
            idx[ch] = i

        idx = [n] * 26
        for i in range(n-1,-1,-1):
            print(i)
            ch = ord(s[i]) - ord('A')
            r.append(idx[ch])
            idx[ch] = i
        
        ans = 0
        for i in range(n):
            # 
            ans += (i - l[i]) * (r[n-i-1] - i)
        
        print(l,r,idx)
        
        return ans

s = Solution()
t = s.uniqueLetterString("LEETCODE")
print(t)