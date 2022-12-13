class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # try，感觉可以用if代替
        last = -1
        numstr = s.split()
        for s in numstr:
            try:
                n = int(s)
            except:
                continue
            else:
                if n <= last:
                    return False
                else:
                    last = n
        return True
