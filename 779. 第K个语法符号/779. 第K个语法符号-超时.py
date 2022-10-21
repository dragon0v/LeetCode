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
        # 获取第n行只要对第n-1行的后一半数进行操作
        # 获取任意行第k个数只需要模拟到第ceil(log2^k)行
        # 模拟法超时
        line = '01'
        n = math.ceil(math.log(k,2))
        # print(2**n)
        for i in range(n):
            line += ''.join(['01' if c=='0' else '10' for c in line[len(line)//2:]])
        return int(line[k-1])

s = Solution()
t = s.kthGrammar(10,1000)
print(t)