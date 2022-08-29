from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        t1 = []
        t2 = []
        for i in range(len(s)):
            if s[i]!=goal[i]:
                t1.append(s[i])
                t2.append(goal[i])
                if len(t1)>2:
                    return False
        if (t1==[] and max(Counter(s).values())>1) or (len(t1)==2 and t1[0]==t2[1] and t1[1]==t2[0]):
            return True
        return False

s = Solution()
t = s.buddyStrings('ab','ab')
print(t)