class Solution:
    def digitCount(self, num: str) -> bool:
        c = [0 for _ in range(10)] # [0] * 10也是一样的
        for d in num:
            c[int(d)] += 1
        print(c)
        for i,d in enumerate(num):
            if c[i]!=int(d):
                #print(c[str(i)],d)
                return False
        
        return True