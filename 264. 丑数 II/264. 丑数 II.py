class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 1,2,3,4,5,6,8,9,10,12
        # =2^i*3^j*5^k
        # 0,0,0 1,0,0 0,1,0 2,0,0 0,0,1 1,1,0 3,0,0
        #   1     2     3     4     5     6     7
        pass