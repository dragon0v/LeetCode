class Solution:
    def minimumBuckets(self, street: str) -> int:
        # HHH xHH HHx
        s = list(street)
        l = len(s)
        res = 0
        i = 0
        while i<l:
            a = l-i
            if a==1:
                if s[i]=='H':
                    return -1
                return res
            elif a==2:
                if s[i:i+2]=='.H' or s[i:i+2]=='H.':
                    res += 1
                    return res
                elif s[i:i+2]=='HH':
                    return -1
                else: #..
                    return res
            elif a>=3:
                t = s[i:i+3]
                # ... ..H .H. H.. .HH H.H HH. HHH
                if t=='...':
                    i += 2
                elif t in ['H..','.HH','.H.']:
                    res += 1
                    i += 2
                elif t in ['HH.','HHH']:
                    return -1
                elif t in ['..H']:
                    t += 1
                elif t in ['H.H']:
                    res += 1
                    i += 3
                
        return res
        
s = Solution().minimumBuckets('H.H')
print(s)