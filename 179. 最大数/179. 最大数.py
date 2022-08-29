class Solution:
    def largestNumber(self, nums]) -> str:
        strs = [str(i) for i in nums]
        def mysort(strs):
            # like pop sort
            # 3,32,322,332,324,330 -> 322,32(322),324,330,332,3(333)
            strs.sort()
            for i in range(len(strs)-1):
                if len(strs[i])!=len(strs[i+1]):
                    strs[i] = max(strs[i]+strs[i+1],strs[i+1]+strs[i])
                    strs[i+1] = ''
                    i += 1
            return strs
        print(strs)
        return ''.join(mysort(strs)[::-1])