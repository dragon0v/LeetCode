class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if(strs==[]):
            return ''
        for i in range(200):
            try:
                if(strs[0]==''):
                    return ''
                else:
                    prfx = strs[0][0:i+1]
                for each in strs:
                    if each == '':
                        return ''
                    else:
                        if(prfx!=each[0:i+1]):
                            if(i==0):
                                return ''
                            else:
                                return strs[0][0:i]
            except:
                return prfx

s = Solution()
r = s.longestCommonPrefix(['sss','sss'])
print(r)
