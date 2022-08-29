class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 以7为例，
        # 可能出现1234567的全排列
        # =C9,7 * A7,7
        # + 9选1作为最高位+带0的6位全排列 
        # =9 * C8,5 *A5,5 * 6
        
        # 10个里面取7个，结果乘0.9
        def C(a,b):
            ret = 1
            for i in range(b):
                ret *= a
                a -= 1
                ret /= i+1
            print('C',a+b,b,ret)
            return ret
        def A(a,b):
            ret = 1
            for i in range(b):
                ret *= a
                a -= 1
            print('A',a+b,b,ret)
            return ret

        # return C(9,n)*A(n,n) + 9*C(8,n-2)*A(n-2,n-2)*(n-1)
        def T(n):
            return C(10,n)*A(n,n)*0.9
        if n==0:
            return 0
        return int(10+sum(T(i) for i in range(2,n+1)))
            
    
s = Solution().countNumbersWithUniqueDigits(7)
print(s)