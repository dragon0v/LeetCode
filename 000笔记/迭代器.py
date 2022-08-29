# 自己实现的类似range的iterator
class MyRange(object):
    def __init__(self,end):
        self.start = 0
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            ret = self.start
            self.start += 1
            return ret
        else:
            raise StopIteration


from collections.abc import *
a = MyRange(5)
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
for i in a:
    print(i)
b = MyRange(2)
print(next(b))
print(next(b))
print(next(b)) # 报错