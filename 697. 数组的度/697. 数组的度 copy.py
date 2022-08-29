class Solution:
    def findShortestSubArray(self, nums):
        # 获取数组的度
        numscnt = [0] * 50000
        maxnums = []
        maxcnt = 0 # 次数超过maxcnt-1就加入maxnums
        for v in nums:
            numscnt[v] += 1
            if(numscnt[v]==maxcnt):
                maxnums.append(v)
            elif(numscnt[v]>maxcnt):
                maxnums = [v]
                maxcnt += 1
        print(maxnums,maxcnt)
        
        # 滑动窗口找最短连续子数组
        i=j=0
        avail = []
        shortest = 50005
        for n,v in enumerate(nums):
            print(i,j,shortest)
            if(v in maxnums):
                avail.append(n)
                if(len(avail)==maxcnt): # 相同度的子数组已经找到
                    shortest = min(shortest,j-i+1)
                    if(shortest==maxcnt):
                        return shortest # 最小值已经是度数，直接返回
                    i = avail.pop(0)
            else:
                if(avail==[]):
                    i+=1
            j+=1
        
        shortest = min(shortest,j-i+1)
        return shortest
            
            
# 题目看错了

s = Solution()
print(s.findShortestSubArray([1,2,2,3,1,4,2]))