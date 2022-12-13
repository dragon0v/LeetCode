from functools import reduce


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # 代码简洁一点，时间还加倍了
        nums = list(map(int, filter(lambda x:'0'<=x[0]<='9',s.split())))
        return all([nums[i]<nums[i+1] for i in range(len(nums)-1)])