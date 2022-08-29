class Solution:
    def minKBitFlips(self, A, K):
        n = len(A)
        N = n # 当前A数组长度
        cnt = 0
        
        while(N-K >= 0):
            if(A[0] == 1):
                A.pop(0)
                N -= 1
            else:
                for i,d in enumerate(A[0:K]):
                    A[i] = (d+1)%2
                cnt += 1
        
        if(A == [1]*(K-1)):
            return cnt
        else:
            return -1
s = Solution()
r = s.minKBitFlips([0,0,0,1,0,1,1,0],3)
print(r)

# 超时，因为真实地进行了翻转