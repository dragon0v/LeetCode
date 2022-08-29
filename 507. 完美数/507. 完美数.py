from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def fact(n):
            if n==1:
                return[0]
            ret = [1]
            for i in range(2,int(sqrt(n))+1):
                if n%i==0:
                    ret.append(i)
                    ret.append(n//i)
            return ret
        return num==sum(fact(num))