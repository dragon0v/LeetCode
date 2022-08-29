class Solution:
    def clumsy(self, N):
        # (n+2)*(n+1)//n = n+3
        # clumsy(10) = 10 * 9 / 8 [+ 7 - 6 * 5 / 4] + 3 - 2 * 1
        #            = 11+7-7+3-2*1
        # 第一个*/组合取正，其余*/组合取负
        # 所有中间的*/组合的结果都和前一个+抵消，从/3开始
        # /2的情况这样算会多1，/1会多2，可以后期做修正
        
        # clumsy(4) = 4 * 3 / 2 + 1
        # clumsy(5) = 5 * 4 / 3 + 2 - 1
        # clumsy(6) = 6 * 5 / 4 + 3 - 2 * 1
        # clumsy(7) = 7 * 6 / 5 + 4 - 3 * 2 / 1 = 8+4-6
        
        def myeval(nums):
            # 优化思路见官方解
            n = len(nums)
            if n==1:
                return nums[0]
            elif n==2:
                return nums[0]*nums[1]
            elif n==3:
                return nums[0]*nums[1]//nums[2]
            elif n==4:
                return nums[0]*nums[1]//nums[2]+nums[3]
            elif n==5:
                return nums[0]*nums[1]//nums[2]+nums[3]-nums[4]
            elif n==6:
                return nums[0]*nums[1]//nums[2]+nums[3]-nums[4]*nums[5]
            else:
                print('panic')
            
            
        nums=[]
        fix = 0
        if N < 7:
            nums = [i for i in range(N,0,-1)]
            # assert len(nums) == N
        else:
            
            t = (N+1)%4
            nums = [i for i in range(N,N-3,-1)] + [j for j in range(t,0,-1)]
            # 修正/2 /1情况
            if t == 0:
                fix = -2
            elif t == 1:
                fix = -1
        print(nums,fix)
        

        
        return myeval(nums) + fix

# 这个代码应该是时间非常快的，复杂度O(6)，但是写的不漂亮，*此后删除*而且是小学生都会的做法，体现不出说明算法的思想
# 这个方法叫数学法，

# 优化思路见官方数学法，由于数字确定，许多表达式的值是确定的

# 2021-4-1 08:58:53 愚人节快乐

s = Solution().clumsy(4)
print(s)