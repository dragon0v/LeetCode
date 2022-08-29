class Solution:
    def minimumBuckets(self, street: str) -> int:
        # HHH xHH HHx
        s = list(street)
        res = 0
        while len(s)>0:
            #print(s)
            if s[0]=='.':
                if len(s)==1 or (len(s)>1 and s[1]=='.'):
                    s.pop(0)
                else:
                    # .H.H .HH
                    if len(s)==2:
                        res += 1
                        s.pop(0)
                        s.pop(0)
                    else:
                        if s[2]=='.': # .H.
                            if len(s)==3:
                                res += 1
                                s.pop(0)
                                s.pop(0)
                                s.pop(0)
                            else:
                                if s[3]=='.':
                                    res += 1
                                    s.pop(0)
                                    s.pop(0)
                                    s.pop(0)
                                else:
                                    res += 1
                                    s.pop(0)
                                    s.pop(0)
                                    s.pop(0)
                                    s.pop(0)
                        else:
                            res += 1
                            s.pop(0)
                            s.pop(0)
            else:
                if len(s)==1 or (len(s)>1 and s[1])=='H':
                    return -1
                else: #H.
                    if len(s)==2:
                        res+=1
                        s.pop(0)
                        s.pop(0)
                    else:
                        if s[2]=='.':
                            res += 1
                            s.pop(0)
                            s.pop(0)
                        else:
                            res += 1
                            s.pop(0)
                            s.pop(0)
                            s.pop(0)
        return res
                    