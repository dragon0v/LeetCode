import heapq
# python标准库
# 不同于其他语言的堆标准库，python的堆为最小堆
# 数据结构中定义堆是一个二叉树，每个父节点的值都只会小于或等于所有孩子结点的值
# heapq使用数组实现，从0开始计数，
# 对所有的k，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]


# 0. 创建一个堆
heap1 = []
heap2 = [1,3,4,5,2,3,6,7,4,8,9]
heapq.heapify(heap2)
print(type(heap1),type(heap2))
print(heap2)
# heap2.sort()
# print(heap2)

# 1. heapq.heappush(heap, item)
# 将 item 的值加入 heap 中，保持堆的不变性
heapq.heappush(heap1,8)

print(heap1)

# 2. heapq.heappop(heap)
# 弹出并返回 heap 的最小的元素，保持堆的不变性
# 如果堆为空，抛出 IndexError
# 使用 heap[0] ，可以只访问最小的元素而不弹出它
heapq.heappop(heap1)
print(heap1)
# heapq.heappop(heap1) 报IndexError

# 3. heapq.heappushpop(heap)
# 将 item 放入堆中，然后弹出并返回 heap 的最小元素（先进后出）
# 该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
heapq.heappush(heap1,4)
heapq.heappush(heap1,5)
heapq.heappush(heap1,6)
print(heap1)
heapq.heappushpop(heap1,9)
print(heap1)
heapq.heappushpop(heap1,-1) # 先进后出，所以进入的如果是最小的就没变化
print(heap1)

# 4. heapq.heapify(x)
# 将list x 转换成堆，原地，线性时间内
heapq.heapify(heap2)

# 5. heapq.heapreplace(heap)
# 弹出并返回 heap 中最小的一项，同时推入新的 item （先出后进）堆的大小不变
# 如果堆为空则引发 IndexError。
# 这个单步骤操作比 heappop() 加 heappush() 更高效，并且在使用固定大小的堆时更为适宜
# pop/push 组合总是会从堆中返回一个元素并将其替换为 item。

heapq.heapreplace(heap1,11)
print(heap1)
heapq.heapreplace(heap1,-1) # 先出后进，所以进入的如果是最小的也有变化
print(heap1)

# 6. heapq.merge(*iterables, key=None, reverse=False)
# 将多个已排序的输入合并为一个已排序的输出（例如，合并来自多个日志文件的带时间戳的条目）
# 返回已排序值的 iterator。

# 7.8. heapq.nlargest/nsmallest(m,iterable,key=None)
# 从iterable里返回n个最大/小元素组成的列表
# 等价于: sorted(iterable, key=key, reverse=True/False)[:n]
# 在 n 值较小时性能最好, 对于更大的n，使用 sorted() 函数会更有效率
# 此外，当 n==1 时，使用内置的 min() 和 max() 函数会更有效率
# 如果需要重复使用这些函数，请考虑将可迭代对象转为真正的堆 -?
heapq.heappush(heap1,4)
heapq.heappush(heap1,5)  
heapq.heappush(heap1,6)
print(heap1)
print(heapq.nlargest(3,heap1))
print(heapq.nsmallest(3,heap1))

# 输入是iterable，并不要求已经heapify
print(heapq.nlargest(3,[i for i in range(10)]))

# 堆排序示例，不稳定排序
def heapsort(iterable):
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for i in range(len(iterable))]

print(heapsort([1,2,4,5,7,4,3,2,6,7,1,4,3,9]))
