class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        (x^y)>>i 将异或结果的第i位移到最低位，高位补0
         & 1(00000...001) 获得最低位结果
        '''
        return sum(((x^y)>>i & 1) for i in range(31))
    