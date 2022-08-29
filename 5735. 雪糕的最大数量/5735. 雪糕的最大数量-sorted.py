class Solution:
    def maxIceCream(self, costs, coins):
        ret = 0
        for i in sorted(costs):
            if coins >= i:
                ret += 1
                coins -= i
            else:
                break
        return ret

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars/solution/5735xue-gao-de-zui-da-shu-liang-zhe-chon-kt3f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
# 一分钟的题，关键是看sorted用法

# sort只能用在list；sorted可以对所有iterable对象进行排序
# list.sort()在原列表上操作；sorted(iterable)返回新的列表

# sorted 语法：

# sorted(iterable, cmp=None, key=None, reverse=False)
# 参数说明：

# iterable -- 可迭代对象。
# cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

# 以下实例展示了 sorted 的使用方法：

# >>>a = [5,7,6,3,4,1,2]
# >>> b = sorted(a)       # 保留原列表
# >>> a 
# [5, 7, 6, 3, 4, 1, 2]
# >>> b
# [1, 2, 3, 4, 5, 6, 7]
 
# >>> L=[('b',2),('a',1),('c',3),('d',4)]
# >>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# >>> sorted(L, key=lambda x:x[1])               # 利用key
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
 
 
# >>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# >>> sorted(students, key=lambda s: s[2])            # 按年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
 
# >>> sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# >>>
# https://www.runoob.com/python/python-func-sorted.html