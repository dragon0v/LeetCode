import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        '''
        0
        01
        0110
        01101001
        0110100110010110
        01101001100101101001011001101001
        '''
        # 找规律：
        # 1. 第n行前一半和第n-1行相同
        # 2. 第n行后一半和第n-1行相反
        # 获取任意行第k个数只需要模拟到第ceil(log2^k)行
        # g(n,k) = ~g(n-1,k-len/2)
        line = '0110'
        n = math.ceil(math.log(k,2))  # 经过此操作后k的位置一定是line(n)的后半段
        # print(2**n)
        for i in range(n-2):
            
        return int(line[k-1])

s = Solution()
t = s.kthGrammar(10,1000)
print(t)