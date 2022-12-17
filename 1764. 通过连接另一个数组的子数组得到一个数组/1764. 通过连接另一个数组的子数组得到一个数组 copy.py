class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # 暴力，能过，时间空间10%
        # for和while循环可以用else，进入else的条件是循环正常退出没有被break，相当于一个自带的flag
        ci = 0
        for g in groups:
            l = len(g)
            for i in range(ci,len(nums)):
                print(nums[i:i+l], g)
                if nums[i:i+l] == g:
                    ci = i+l
                    break
            else:
                return False
        return True
        6