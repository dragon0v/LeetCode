class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # if
        last = -1
        numstr = s.split()
        for s in numstr:
            if s.isnumeric():
                n = int(s)
                if n<=last:
                    return False
                last = n
        return True
