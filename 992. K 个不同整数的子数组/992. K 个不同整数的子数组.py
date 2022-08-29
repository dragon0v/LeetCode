class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        n = len(A)
        count = 0
        for i in range(n-K+1):
            s = list(set(A[i:i+K]))
            n2 = len(s)
            avail = K - n2 # 剩余能容纳新的数字数,=0说明已经为满足条件的状态
            t=K
            if avail == 0: # 上一次结果满足条件
                #print(A[i:i+t])
                count += 1
            
            for each in A[i+K:n]:
                #print(each)
                if each not in s: # 有新数字
                    if avail > 0: # 有余量
                        avail -= 1
                        s.append(each)
                        if avail == 0: # 上一次结果满足条件
                            #print(A[i:i+t+1])
                            count += 1
                        #count += 1
                    else:
                        break
                else:
                    if avail == 0: # 上一次结果满足条件
                        #print(A[i:i+t+1])
                        count += 1
                t += 1
        return count

s = Solution()
print(s.subarraysWithKDistinct([1,2,1,1,2,3],2))
#大数据会超时