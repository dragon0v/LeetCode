class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 分类讨论+归纳
        # 1. k=0，只有一种状态
        # 2. k>0,
        # 2.1 n=1，能做到亮灭两种状态
        # 2.2 n=2，若k=1，有3种状态；若k=2，可取得全部4种状态
        # 2.3 n>3，四种操作会使得灯泡每6组一循环，只需考虑n=3~6的情况，而当n=4,5,6时，新引入的灯泡状态由前三个灯泡唯一确定
        if presses==0:
            return 1
        if n==1:
            return 2
        if n==2:
            return 3 if presses==1 else 4
        else:
            # return 4 if presses==1 else 7 if presses==2 else 8
            if presses==1:
                return 4
            if presses==2:
                return 7
            else:
                return 8
        