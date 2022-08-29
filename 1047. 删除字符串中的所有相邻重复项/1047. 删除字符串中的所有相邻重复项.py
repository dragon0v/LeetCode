class Solution:
    def removeDuplicates(self, S):
        mystack = []
        res = ''
        for c in S:
            if not mystack:
                mystack.append(c)
            elif mystack and mystack[-1] != c:
                mystack.append(c)
            elif mystack[-1] == c:
                mystack.pop(-1)
        return ''.join(mystack)

s = Solution()
t = s.removeDuplicates("abbacds")
print(t)
