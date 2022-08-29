class Solution:
    def checkPossibility(self, nums) -> bool:
        if len(nums)<=2:
            return True
        
        # 保证每次都是局部非递减的
        # 优先调整前一个，不能调整在调整当前的
        # 瞻前顾后，每次看三个元素
        changed = False
        for i in range(len(nums)):
            if i==0 and nums[1] < nums[0]:
                nums[0] = -100001
                changed = True
            if i>0 and nums[i] < nums[i-1]:
                if changed:
                    print(i)
                    return False
                elif nums[i-1]>nums[i-2] and nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i-2]
                elif i == 1:
                    nums[0] = -1000001
                else:
                    nums[i] = nums[i-1]
                    changed = True
        
        return True

s = Solution()
t = s.checkPossibility([1,2,3,3,2,3,5,8])
print(t)
t = s.checkPossibility([4,1,2,3,3,3,5,8])
print(t)
t = s.checkPossibility([-1,4,2,3])
print(t)
t = s.checkPossibility([4,2,1])
print(t)
t = s.checkPossibility([1,5,4,6,7,10,8,9])
print(t)