class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 写了个计算m的函数，算是不那么屎了
        def getSum(t):
            m = 0
            # index左边求和，不包含index
            if t>=index:
                # 按等差数列求和
                m += (t-index+t-1)*(index-0)/2
            else:
                # 部分按等差数列求和，其余是1
                m += (t-1)*t/2+(index-t+1)
            # index和index右边求和
            if t>= n-index:
                m += (t+t-(n-1-index))*(n-index)/2
            else:
                m += (t+1)*t/2+(n-index-t)
            return m

        # 贪心+二分
        i,j = 0, maxSum
        while i<j:
            print(i,j)
            t = (i+j) // 2
            m = getSum(t)
            if m<=maxSum:
                i = t+1
            else:
                j = t-1

        t = t+1
        while 1:
            m = getSum(t)
            if m<=maxSum:
                return t
            else:
                t -= 1
            