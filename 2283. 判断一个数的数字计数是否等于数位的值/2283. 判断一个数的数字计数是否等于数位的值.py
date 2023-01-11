class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        print(c)
        for i,d in enumerate(num):
            if c[str(i)]!=int(d):
                return False
        
        return True