class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        word += 'a'  # 可以省下最后判断t是否非空的代码
        t = ''
        for c in word:
            if c in '1234567890':
                t += c
            else:
                if t:
                    nums.add(int(t))
                    t = ''
        return len(nums)