# 输出最少的步数，如果不存在方案，则输出-1。
# 样例输入
# 12345678. 
# 123.46758 
# 样例输出
# 3

# https://blog.csdn.net/XIAOQINGJ/article/details/107512893
# https://www.dotcpp.com/oj/problem1426.html

# 采用广度优先搜索BFS

class Solution:
    def __init__(self,o,t):
        assert len(o) == len(t) and len(o) == 9
        self.ori = [[o[0],o[1],o[2]],
                    [o[3],o[4],o[5]],
                    [o[6],o[7],o[8]],]
        self.target = [[t[0],t[1],t[2]],
                       [t[3],t[4],t[5]],
                       [t[6],t[7],t[8]],]
        self.res = 1000 # 最少步数
    def arrange(self):
        pass

s = Solution('12345678.','123.45678').arrange()
print(s)