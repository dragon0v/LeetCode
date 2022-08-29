class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = []
        for c in s1:
            chars.append(c)
        n = len(s1)
        for i in range(len(s2)-n+1):
            t = s2[i:i+n]
            tchars = chars
            flag = True
            for c in t:
                if c in tchars:
                    tchars.remove(c)
                else:
                    flag = False
                    print(c,t)
                    break
            if flag:
                return True
                    
        
        return False

s = Solution().checkInclusion('abc','bcba')
print(s)
# TODO 