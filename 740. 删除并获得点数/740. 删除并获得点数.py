class Solution:
    def deleteAndEarn(self, nums) -> int:
        # 直接删除全部单独出现的数字
        # 对于所有连续出现的数字们，
        n = list(set(nums))
        print(n)
        
# TODO 做完三题打家劫舍这题就会了