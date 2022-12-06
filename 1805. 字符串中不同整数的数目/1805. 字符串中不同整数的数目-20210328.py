class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = []
        n = ''
        for c in word:
            if c in '0123456789':
                n += c
            else:
                if n!='':
                    nn = int(n)
                    if nn not in nums:
                        nums.append(nn)
                n = ''
        if n!='':
            nn = int(n)
            if nn not in nums:
                nums.append(nn)
        print(nums)
        return len(nums)