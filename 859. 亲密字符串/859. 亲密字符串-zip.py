from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 1. 长度不一样返回false
        if len(s)!=len(goal):
            return False
        # 2. 相同字符串，s中需要有重复出现的字符
        if s==goal:
            if len(set(s))!=len(s):
                return True
            return False
        # 3. 用zip获得s和goal的不同
        diff = [(a,b) for a,b in zip(s,goal) if a!=b]
        return len(diff)==2 and diff[0][0]==diff[1][1] and diff[0][1]==diff[1][0]

s = Solution()
t = s.buddyStrings('ab','ab')
print(t)
t = s.buddyStrings('aa','aa')
print(t)