from itertools import *
# https://blog.csdn.net/neweastsun/article/details/51965226
# itertools中的class所有的返回值都是iterable

# ----------------------------------
# 1. chain：把多个iterable链接在一起
# ----------------------------------
a = [1,2,3,4,5]
b = ("sd","ds","fgg")
c = [True,False]
for each in chain(a,b,c):
    print(each,end = ' ')
print(list(chain(a,b,c)))

# ----------------------------------
# 2. count(start=0,step=1)：生成无限的序列，必须手动break
# ----------------------------------
for each in count(100,3):
    print(each)
    if each>110:break
    
# ----------------------------------
# 3. filter/filterfalse(contintion,data)：
# 迭代过滤条件为True的数据。如果条件为空，返回data中为True的项；
# 迭代过滤条件为false的数据。如果条件为空，返回data中为false的项；
# ----------------------------------
d = [1,2,0,11,222,True,False,'','asd',{'1':3},{},None,lambda a,b:a+b]
print(list(filterfalse(None,d))) #没有给定条件，返回d中为false的项
print(list(filter(lambda x:type(x)==int and x>3,d)))
print(list(filterfalse(lambda x:type(x)!=int or x<3,d)))

# ----------------------------------
# 4. compress(data,selectors)：
# 根据selectors中的真值，返回data中对应的元素
# ----------------------------------
print(list(compress([1,2,3,4],[True,False,0,1,1,1,1])))# 长度不一致按最短的匹配

# ----------------------------------
# 5. starmap(func,list)：对list的*每一项*调用func
# ----------------------------------
print(list(starmap(pow,[(1,2),(3,4),(5,6)])))
print(list(starmap(max,[(1,2,3),(3,4,5),(7,8,9)])))
def foo(*args):
    n = len(args)
    return args[int(n*0.25)+1:int(n*0.75)]
print(list(starmap(foo,[(3,2,1),(3,4,5,6,7,8,9),(100,102,103,7,8,9)])))
print(list(starmap(lambda s1,s2,s3:s2+s1+s3,[("asd"),("xyz"),("abc")])))

# ----------------------------------
# 6. repeat(object,times)：重复objecttimes遍
# ----------------------------------
print(list(repeat(10,3)))

# ----------------------------------
# 7. dropwhile(func,seq)：当func返回假时开始迭代序列
# 8. takewhile(func,seq)：一直迭代序列直到func返回假
# ----------------------------------
print(list(dropwhile(lambda s:s!='start',['1','2','start','3','4','end','5','6'])))
print(list(takewhile(lambda s:s!='end',['1','2','start','3','4','end','5','6'])))

# ----------------------------------
# 9. islice(seq[,start],stop[,step])
# 返回序列seq的从start开始到stop结束的步长为step的元素的迭代器
# ----------------------------------
print(list(islice('abcdefghij',0,8,2)))

# ----------------------------------
# 10. product(iter1,iter2, ... iterN, [repeat=1])
# 生成表示item1，item2等中的项目的笛卡尔积的元组，重复repeat次
# ----------------------------------
print(list(product('ABCD', 'xy'))) # --> Ax Ay Bx By Cx Cy Dx Dy))
print(list(product(range(2), repeat=3))) # --> 000 001 010 011 100 101 110 111

# ----------------------------------
# 11. permutations(p,r)
# 返回p中任意取r个元素做排列的元组的迭代器
# ----------------------------------
print(list(permutations(range(3),2)))

# ----------------------------------
# 12. combinations(iterable,r)
# 返回iterable中所有长度为r的子序列，保留相对顺序
# 13. combinations_with_replacement(iterable,r)
# 返回iterable中所有长度为r的子序列，保留相对顺序，元素可以重复使用
# ----------------------------------
print(list(combinations([1,2,3,4],3)))
print(list(combinations_with_replacement([1,2,3,4],3)))

# 在列表中找到三个和为13的数
for pairs in list(combinations([1,2,5,65,7,3,4,6,3,2],3)):
    if sum(pairs)==13:
        print(pairs,end=' ')
print()









