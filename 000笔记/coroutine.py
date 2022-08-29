# https://zhuanlan.zhihu.com/p/27258289
# 1. 普通函数
def function():
    return 1
# 2. 生成器函数
def generator():
    yield 1
# 3. 异步函数
async def async_function():
    return 1
# 4. 异步生成器
async def async_generator():
    yield 1

# 判断函数类型
# import types
# TODO 为什么有的加括号有的不加（改了就变false
# print(type(function) is types.FunctionType)
# print(type(generator()) is types.GeneratorType)
# print(type(async_function()) is types.CoroutineType)
# print(type(async_generator()) is types.AsyncGeneratorType)

# 直接调用异步函数不会返回结果，而是返回一个coroutine对象
print(async_function()) # <coroutine object async_function at 0x000001E5EAA70448>
# 协程需要通过其他方式来驱动，因此可以使用这个协程对象的send方法给协程发送一个值
print(async_function().send(None))



