# 阿里面试题2022-3-25
# 可以先做560. 和为K的子数组

# 思路：连续子数组考虑前缀和
# 如果presum[j]-presum[i] % k == 0，即说明从i到j是一个符合要求的子数组

from typing import *
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0:1}  # 记录在当前num之前的所有对k取余的值
        last = 0  # 记录当前num前的前缀和对k取余的值
        res = 0
        for num in nums:
            mod = (last+num)%k
            last = mod
            recorded = record.get(mod,0)  # get方法相比dict[key]可以指定key缺失时的默认值，而后者会报错
            res += recorded
            record[mod] = recorded + 1  # 指定recorded变量，避免在此处判断mod在不在keys中
            
        return res
        
        
s = Solution().subarraysDivByK([4,5,0,-2,-3,1],5)
print(s)