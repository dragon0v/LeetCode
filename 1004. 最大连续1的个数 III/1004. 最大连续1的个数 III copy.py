class Solution:
    def longestOnes(self, A, K):
        #滑动窗口，
        N = len(A)
        i = 0
        j = 0
        res = fc = 0 # res是返回的最大值，t是当前窗口最大值=j-i+1，fc是已经改变的0个数=len(flipped)
        flipped = [] # 存放在滑动过程中改变的K个0
        
        # 特例情况
        if(K==0):
            for u,v in enumerate(A):
                if(v==0):
                    res = max(res,j)
                    j=0
                else:
                    j += 1
            return max(res,j)
        
        # 正常情况
        for u,v in enumerate(A):
            #print(i,j,flipped,res)
            if(v==0): # 遇到0
                if(fc<K): # 还可以翻转
                    flipped.append(u)
                    fc += 1
                else: # 已经不能翻转了
                    res = max(res,j-i+1)
                    i = flipped.pop(0) + 1 # 移动左窗口
                    
                    flipped.append(u) # 因为遇到0，所以也要翻转的
            else: # 是1，窗口向右滑动
                pass
            j = u
        res = max(res,j-i+1)
        return res
s = Solution()
# print(s.longestOnes([0,0,0],0))
print(s.longestOnes([0,0,0,0,0,1,1,0,0,0,0,1,1,1,1],3))
                
                    