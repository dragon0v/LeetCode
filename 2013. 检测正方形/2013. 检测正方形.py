from collections import defaultdict, Counter
from typing import *
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(Counter)


    def add(self, point: List[int]) -> None:
        # 数据结构是dict(x: dict(y: 点(x,y)的个数))
        # 要获取点(x,y)的个数可以用points[x][y]
        x,y = point
        self.points[x][y] += 1
        print(self.points)

    def count(self, point: List[int]) -> int:
        # 拿到xy坐标后，找有哪些x坐标相同的点，则y坐标差值就是正方形边长，然后找有没有符合条件的其他两个点
        '''
        obj.add([3,10])
        obj.add([11,2])
        obj.add([3,2])
        param_2 = obj.count([11,10])
        1. 找到x坐标为11，且y不为10的所有点 xxx=self.points[x]
        2. 得到正方形边长 a=abs(k-y)
        3. 看是否有满足条件的其他两个点
        '''
        x,y = point
        res = 0
        if x not in self.points.keys():
            return 0
        
        xxx =  self.points[x]  # 所有坐标为x的y坐标们
        for k,v in xxx.items():  # k是存在的y坐标们，v是点(x,y)的个数
            if k!=y:
                a = abs(k-y)  # 正方形边长
                # 四个点(x,y),(x,k),(x+a,y),(x+a,k)
                res += self.points[x][k] * self.points[x+a][k] * self.points[x+a][y]
                res += self.points[x][k] * self.points[x-a][k] * self.points[x-a][y]

        return res





# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
param_2 = obj.count([11,10])
print(param_2)
param_2 = obj.count([14,8])
print(param_2)
obj.add([11,2])
param_2 = obj.count([11,10])
print(param_2)

