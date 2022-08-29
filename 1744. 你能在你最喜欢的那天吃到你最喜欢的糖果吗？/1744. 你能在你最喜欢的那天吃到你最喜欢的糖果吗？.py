class Solution:
    def canEat(self, candiesCount, queries):
        # 到第i天（i从0开始），已经吃的糖果范围为[i-1,(i-1)*dailyCap]
        # 第i天可以吃到的糖果范围为[i,i*dailyCap]
        # 前缀和 
        ans = []

        # 这里用了比较复杂的，可以用presum[i-1]+candiesCount[i]
        # 哈哈然后超时了
        '''
        preSum = [sum(candiesCount[:i]) for i in range(len(candiesCount)+1)]
        print(preSum)
        # [0, 7, 11, 16, 19, 27]
        '''
        preSum = [0]
        for i in range(len(candiesCount)):
            preSum.append(preSum[i]+candiesCount[i])
        print(preSum)

        # 官方解法的preSum用accumulate实现，列表长度和原列表相同，用在我的代码里要加前导0
        from itertools import accumulate
        preSum = [0] + list(accumulate(candiesCount))
        print(preSum)

        for each in queries:
            favoriteType, favoriteDay, dailyCap = each[0],each[1],each[2]
            # 第i天可以吃到的糖果范围
            low1 = favoriteDay + 1 - 1 # 下标，包含
            high1 = (favoriteDay+1)*dailyCap - 1 # 下标，包含
            # 喜欢的糖果范围
            low2 = preSum[favoriteType] # 下标，包含
            high2 = preSum[favoriteType+1] -1 # 下标，包含
            
            # 两端范围有相交即可，这里考虑反面会更容易
            if high1<low2 or low1>high2:
                ans.append(False)
            else:
                ans.append(True)
        return ans

s = Solution()
t = s.canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]])
print(t)