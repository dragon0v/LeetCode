class Solution:
    def reformatNumber(self, number):
        # 一次遍历+修改末尾
        # 123-456-78-90 需要进一步处理
        # 123-456-789 去掉最后一位
        # 123-456-78 可以直接return
        res = '' # 长度2-100
        cnt = 0
        l = 0 #含的数字数
        for c in number:
            if(c!=' ' and c!='-'):
                res += c
                cnt += 1
                l += 1
                if(cnt == 3):
                    cnt = 0
                    res += '-'
        # if (l == 2 or l==5):
        #     return res
        # elif(l==3):
        #     return(res[:-1])
        if(l%3==2):
            return res
        elif (l%3==0):
            return res[:-1]
        elif (l%3 == 1):
            return res[:-5] + res[-5:-3] + '-' + res[-3] + res[-1]
            
s = Solution()
print(s.reformatNumber('1231'))

# 时间击败个位数
# 然后第三次提交一模一样的两个超过90%+。。。