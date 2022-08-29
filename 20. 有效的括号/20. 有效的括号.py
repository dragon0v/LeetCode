class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if(c=='(' or c=='[' or c=='{'):
                stack.append(c)
            elif(c==')'):
                if stack == [] or stack[-1] != '(':
                    return False
                else:
                    del stack[-1]
            elif(c==']'):
                if stack == [] or stack[-1] != '[':
                    return False
                else:
                    del stack[-1]
            elif(c=='}'):
                if stack == [] or stack[-1] != '{':
                    return False
                else:
                    del stack[-1]
        return not stack

s = Solution()
print(s.isValid('{[]}'))