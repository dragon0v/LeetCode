

class Solution:
    def findTheDifference(self, s, t):
        l = [0] * 26
        for c in s:
            l[ord(c)-ord('a')] += 1
        for c in t:
            l[ord(c)-ord('a')] -= 1
            if(l[ord(c)-ord('a')]) == -1:
                return c
            
            
            

s = Solution()
print(s.findTheDifference('s','sr'))

