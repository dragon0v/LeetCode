from bisect import bisect_right
from itertools import chain, combinations, starmap
from typing import *
from operator import add


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # 思路：因为数据量很少，所以直接枚举所有可能
        # 1584ms, 击败14.5%

        # 计算所有topping的组合
        toppings = set()
        toppingCosts += toppingCosts
        n = len(toppingCosts)

        for i in range(1,n+1):
            combs = combinations(toppingCosts,i)
            for comb in combs:
                toppings.add(sum(comb))

        toppings.add(0)  # 一种topping都不加的情况
        
        # print(toppings)

        for base in baseCosts:
            if target-base in toppings:
                return target

        allres = set()
        for base in baseCosts:
            for topping in toppings:
                allres.add(base+topping)
        allres = sorted(list(allres))
        idx = bisect_right(allres,target)
        if idx==0:
            return allres[0]
        if idx==len(allres):
            return allres[-1]
        possible1 = allres[idx]
        possible2 = allres[idx-1]
        if abs(possible1-target)>abs(possible2-target):
            return possible2
        elif abs(possible1-target)<abs(possible2-target):
            return possible1
        else:
            return min(possible2,possible1)

        # 这里想用itertools的函数来一行得出toppings，本来以为挺简单但是失败了
        # toppings = list(map(sum, chain(combinations(toppingCosts,i) for i in range(1,n+1))))
        # t = [combinations(toppingCosts,i) for i in range(1,n+1)]
        # print(list(t))  # [[(),()],[],[]]
        # print(list(combinations(range(3),2)))
        # ttt = starmap(sum, list(combinations(range(3),2)))
        # print(list(ttt))
        # t = [starmap(add,combinations(toppingCosts,i)) for i in range(1,n+1)]
        # print(t)
        # for e in t:
        #     print(list(e))
        # toppings = chain(list([starmap(add,combinations(toppingCosts,i)) for i in range(1,n+1)]))
        # print(list(toppings))

s = Solution()
t = s.closestCost([1,2,3],[4,5,6,7,8],1)
print(t)
t = s.closestCost([1,2,3],[4,5,6,7,8],46)
print(t)
t = s.closestCost([1,2,3],[4,5,6,7,8],100)
print(t)
t = s.closestCost([1,2,3],[4,5,6,7,8],-99)
print(t)
t = s.closestCost([1,2,3],[4,5,6,7,8],59)
print(t)