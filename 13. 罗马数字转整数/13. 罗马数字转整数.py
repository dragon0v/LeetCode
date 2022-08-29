class Solution:
    def romanToInt(self, s):
        res = 0
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        for i,c in enumerate(s):
            res += d[c]
            if i != 0 and c != 'I':
                if last == "I" and c in "VX":
                    res -= 2 # 之前加过一遍1，所以这里要-2
                elif last == "X" and c in "LC":
                    res -= 20
                elif last == "C" and (c in "DM"):
                    res -= 200
            last = c
            print(res,last)
        
        return res


s = Solution()
t = s.romanToInt("MCMXCIV")
print(t)
