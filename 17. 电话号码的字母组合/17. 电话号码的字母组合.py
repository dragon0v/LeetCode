class Solution:
    def letterCombinations(self, digits):
        if digits=="":
            return []
        # 其他语言用哈希表？，python用的是dict
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[] # 所有的结果集
        t=[] # 存放当前的字母顺序
        def backtrack(i):
            # 所有字母都使用了
            if i==len(digits):
                res.append("".join(t))
            else:
                for c in phoneMap[digits[i]]:
                    t.append(c)
                    backtrack(i+1)
                    t.pop(-1) # 换c

        backtrack(0)
        return res

s = Solution()
print(s.letterCombinations('23'))

# 是完全抄参考解的