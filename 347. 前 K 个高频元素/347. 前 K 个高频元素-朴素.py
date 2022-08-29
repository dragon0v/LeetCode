from typing import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            # dict.get(): eturn the value for key if key is in the dictionary, else default.
            counter[n] = counter.get(n,0) + 1
        
        ans = sorted(counter.items(),key=lambda l:l[1])[-k:]
        # return list(map(lambda l:l[0],ans))
        # 不使用map的方法
        return [v[0] for v in ans]
       


# 思路是先遍历读到字典，然后对字典内元素排序得到结果
# 复杂度NlogN
# 按题意，最优的方法应该在Nlogk
s = Solution()
t = s.topKFrequent([1,1,1,2,2,3],2)
print(t)