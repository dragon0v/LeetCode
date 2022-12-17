class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # 暴力，能过，时间空间10%
        ci = 0
        for g in groups:
            flag = False
            l = len(g)
            for i in range(ci,len(nums)):
                print(nums[i:i+l], g)
                if nums[i:i+l] == g:
                    ci = i+l
                    flag = True
                    break
            if not flag:
                return False
        return True
        