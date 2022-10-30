from typing import *
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # dfs，每增加一位字母都会带来两种新结果
        res = []
        n = len(s)

        def dfs(i,crt):
            def other(a):
                # 找到字母的另一个大写/小写
                # 有没有更优雅的方法？
                if ord('A')<=ord(a)<=ord('Z'):
                    return chr(ord('a') + ord(a) - ord('A'))
                return chr(ord('A') + ord(a) - ord('a'))
            # dfs结束条件
            if len(crt)==n:
                res.append(crt)
                return 
            new = s[i]
            if new.isalpha():
                # 是字母，需要增加其大写/小写
                dfs(i+1,crt+other(new))
            dfs(i+1,crt+new)
        
        dfs(0,'')
        return res

s = Solution()
t = s.letterCasePermutation('a1as12983uih')
print(t)