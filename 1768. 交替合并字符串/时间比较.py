# str+str
# ''.join(list)

from timeit import timeit
def f1():
    res = ''
    for i in range(10000):
        res += 'a'
    return res

def f2():
    ans = []
    for i in range(10000):
        ans.append('a')
    return ''.join(ans)

t1 = timeit('f1()', 'from __main__ import f1', number=10000)
t2 = timeit('f2()', 'from __main__ import f2', number=10000)
print(t1, t2)
# 24.3260265 5.5511792