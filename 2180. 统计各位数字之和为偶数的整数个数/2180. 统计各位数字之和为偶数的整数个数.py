class Solution:
    def countEven(self, num: int) -> int:
        def getsum(n):
            s = 0
            while n>0:
                n,ss = divmod(n,10)
                s += ss
            return s%2==0
        
        return len(list(filter(getsum,range(1,num+1))))