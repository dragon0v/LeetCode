class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        必须 原地 修改，只允许使用额外常数空间。
        """

        # 对于一般情况，从后往前找到第一处减小的地方并交换它和仅比他大的数
        last = None
        changed = False
        for i in range(len(nums)-1,-1,-1):
            if last != None and last > nums[i]:
                
                
                changed = True
                break
            last = nums[i]

        # 不存在下一个更大的排列的情况说明nums不增
        # 此时返回nums的逆序即可
        if not changed:
            print(123)
            nums = nums[::-1]
        
        '''
        以下为测试内容
        '''
        return nums

s = Solution()
t = s.nextPermutation([1,2,3,4,3,2,1,6,5,4,3,2,1,1])
print(t)