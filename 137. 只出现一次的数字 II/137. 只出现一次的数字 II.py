class Solution:
    def singleNumber(self, nums) -> int:
        # 上一题是重复两次，使用了异或操作，使最后剩下那个就是答案
        # 这题应该也是这个思路
        
        # 仅当 seen_twice 未变时，改变seen_once。
        # 仅当 seen_once 未变时，改变seen_twice。
        
        # 第一次出现把seen_once置为数，
        # 第二次出现把seen_once置零，seen_twice置为数
        # 第三次出现把seen_twice置零
        seen_once,seen_twice = 0,0
        for n in nums:
            seen_once = ~seen_twice & (seen_once^n)
            seen_twice = ~seen_once & (seen_twice^n)
            
        return seen_once