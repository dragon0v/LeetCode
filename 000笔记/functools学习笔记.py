from functools import *
# functools 模块可以说主要是为函数式编程而设计，用于增强函数功能。

# https://blog.csdn.net/qq_1290259791/article/details/84930850

# --------------------------------------
# 1. partial(func,*args,**keyargs)
# 用于创建一个偏导数，固定住原函数的部分参数
# --------------------------------------
int2 = partial(int,base=16)
print(int2('123'),int('123',base=16))

def add(*args):
    return sum(args)
add_100 = partial(add,100)
add_900 = partial(add,900)
print(add_100(1,2,3,4),add_900(1,2,3,4))

# --------------------------------------
# 2. update_wrapper
# 使用 partial 包装的函数是没有__name__和__doc__属性的。
# update_wrapper 作用：将被包装函数的__name__等属性，拷贝到新的函数中去。
# --------------------------------------
# TODO
def wrap2(func):
	def inner(*args):
		return func(*args)
	return update_wrapper(inner, func)

@wrap2
def demo():
	print('hello world')

print(demo.__name__)

# --------------------------------------
# 3. wraps
# warps 函数是为了在装饰器拷贝被装饰函数的__name__。
# 就是在update_wrapper上进行一个包装
# --------------------------------------
# TODO
def wrap1(func):
	@wraps(func)	# 去掉就会返回inner
	def inner(*args):
		print(func.__name__)
		return func(*args)
	return inner

@wrap1
def demo():
	print('hello world')

print(demo.__name__)

# --------------------------------------
# 4. reduce(function, sequence, startValue)
# 将序列的前两个元素传入func，将结果和第三个元素传入func，如此循环
# --------------------------------------
print(reduce(lambda x,y:x+y, range(50)))
print(reduce(lambda x,y:y+x, "abcdef"))

# --------------------------------------
# 5. cmp_to_key(func)
# 将比较函数（comparison function）转化为关键字函数（key function）
# 主要是用来将程序转换为py3格式的
# --------------------------------------
# TODO
nums = [3, 30, 34, 5, 9]
new_nums = sorted(nums, key=cmp_to_key(lambda x, y: y - x))
new_nums2 = sorted(nums, key=cmp_to_key(lambda x, y: x - y))
print(new_nums)
print(new_nums2)
# 原文链接：https://blog.csdn.net/chl183/article/details/106964281

# --------------------------------------
# 6. lru_cache(max_size,typed=False)
# 允许我们将一个函数的返回值快速地缓存或取消缓存。
# 该装饰器用于缓存函数的调用结果，对于需要多次调用的函数，而且每次调用参数都相同，则可以用该装饰器缓存调用结果，从而加快程序运行。
# max_size设置为2的n次幂时，性能最佳
# lru：队列满时将最近最少被访问的元素移除，
# typed=True会把f(3.0)和f(3)分开缓存，默认False
# 该装饰器会将不同的调用结果缓存在内存中，因此需要注意内存占用问题。
# --------------------------------------
from timeit import timeit

@lru_cache(maxsize=2**18)  # maxsize参数告诉lru_cache缓存最近多少个返回值
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
t1 = timeit('[fib(n) for n in range(10000)]','from __main__ import fib',number=50)
fib.cache_clear()   # 清空缓存

def fib2(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
t2 = timeit('[fib2(n) for n in range(10000)]','from __main__ import fib2',number=50)

print(t1,t2,t2/t1)

# --------------------------------------
# 7. singledispatch
# 单分发器， Python3.4新增，用于实现泛型函数。
# 根据单一参数的类型来判断调用哪个函数。
# --------------------------------------
# TODO
@singledispatch
def fun(text):
	print('String：' + text)

@fun.register(int)
def _(text):
	print(text)

@fun.register(list)
def _(text):
	for k, v in enumerate(text):
		print(k, v)

@fun.register(float)
@fun.register(tuple)
def _(text):
	print('float, tuple')
fun('i am is hubo')
fun(123)
fun(['a','b','c'])
fun(1.23)
print(fun.registry)	# 所有的泛型函数
print(fun.registry[int])	# 获取int的泛型函数














