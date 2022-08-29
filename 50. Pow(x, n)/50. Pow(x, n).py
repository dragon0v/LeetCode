class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # 如果超过100次循环中小数点后6位都相同，则认为可以break?

        ans = 1.000000
        last = 1.000000
        last_cnt = 0
        if n > 0:
            for i in range(n):
                ans *= x
                if last*100000//1 == ans*100000//1:
                    last_cnt += 1
                    if last_cnt > 100:
                        break
                else:
                    last_cnt = 0
        if n < 0:
            for i in range(-n):
                ans /= x
                if last*100000//1 == ans*100000//1:
                    last_cnt += 1
                    if last_cnt > 100:
                        break
                else:
                    last_cnt = 0
                

        return ans

# 超时，并且100次break的判断方法应该是不准确的
# 大于0小于0分开写 没有复用也很傻