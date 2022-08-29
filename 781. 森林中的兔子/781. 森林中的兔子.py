from collections import Counter

class Solution:
    def numRabbits(self, answers):
        if answers == []:
            return 0
        c = Counter(answers)
        ans = 0
        for k in c.keys():
            v = c[k]
            if v <= k+1:
                ans += k+1
            else:
                t=v//(k+1)
                if v % (k+1) == 0:
                    ans += t * (k+1)
                else:
                    # [10,10,2,2,2,2,2,2,2,2,2]
                    # 回答2个10，最少11只
                    # 回答9个2,3个一组，3组，所以9只

                    # [1,1,0,0,0]
                    # 2个1，2只
                    # 每个0一只，共3只
                    ans += (t+1)*(k+1)
                    print(t,k)

        return ans

# 不需要前面的if应该也可以
