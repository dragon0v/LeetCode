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
                else:
                    j += 1
            return res
        # 正常情况
        # for u,v in enumerate(A):
        #     print(i,j,flipped)
        #     if(v==0):
        #         if(fc<K): #当前窗口还有余位
        #             flipped.append(u)
        #             fc += 1
        #             if(j<N-1):
        #                 j += 1 # 窗口右侧右移一位
        #             else:
        #                 res = max(res,j-i+1)
        #         else: # 当前窗口已无余位
        #             # 当前窗口结束
        #             res = max(res,j-i+1)
        #             i = flipped.pop(0) + 1 #窗口左侧变成最先变的0的下一位
        #             fc -= 1
        #             #新的窗口开始
        #             flipped.append(u)
        #             fc += 1
        #     else: # 是1，则窗口右侧右移
        #         if(j<N-1):
        #             j += 1 # 窗口右侧右移一位
        #         else:
        #             res = max(res,j-i+1)
        # return res
        while(j<N-1):
            print(i,j,flipped)
            if(A[j]==0):
                if(fc<K): #当前窗口还有余位
                    flipped.append(j)
                    fc += 1
                    if(j<N-1):
                        j += 1 # 窗口右侧右移一位
                    else:
                        res = max(res,j-i+1)
                else: # 当前窗口已无余位
                    # 当前窗口结束
                    res = max(res,j-i+1)
                    i = flipped.pop(0) + 1 #窗口左侧变成最先变的0的下一位
                    fc -= 1
                    #新的窗口开始
                    flipped.append(j)
                    fc += 1
                    j += 1
            else: # 是1，则窗口右侧右移
                if(j<N-1):
                    j += 1 # 窗口右侧右移一位
                else:
                    res = max(res,j-i+1)
        return res
            
s = Solution()
# print(s.longestOnes([0,0,0],0))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
                
                    