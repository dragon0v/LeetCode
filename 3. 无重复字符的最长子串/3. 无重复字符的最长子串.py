class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_appear = [-1 for i in range(128)] # 储存一个字符最后出现的下标
        res = 0 # 最长子串
        t = 0
        for i,c in enumerate(s):
            if last_appear[ord(c)] == -1:
                last_appear[ord(c)] = i
                t += 1
            else:
                res = max(res,t)
                t = i-last_appear[ord(c)]
                last_appear[ord(c)] = i

                last_appear = [-1 for i in range(128)]
                for j in range(t):
                    last_appear[ord(s[i-t+j])] = i-t+j

        res = max(res,t) # 老是忘掉这个

        return res


s = Solution().lengthOfLongestSubstring('aaa')
print(s)
# TODO，不成功


