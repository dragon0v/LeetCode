class Solution:
    def secondHighest(self, s: str) -> int:
        flag = False
        for c in '9876543210':
            if c in s:
                if flag:
                    return int(c)
                else:
                    flag = True
        return -1