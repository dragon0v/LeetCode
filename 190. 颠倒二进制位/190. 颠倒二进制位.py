class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        # 由于有前导0，所以一定是循环32次
        for i in range(32):
            # print(n%2)
            r = r*2 + n%2
            n = n//2
            
        
        return r