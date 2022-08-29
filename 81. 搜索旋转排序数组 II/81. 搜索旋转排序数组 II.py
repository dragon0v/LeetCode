class Solution:
    def search(self, nums, target: int) -> bool:
        # 拼回去后对分查找
        newnums = []
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i]>nums[i+1]:
                newnums = nums[i+1:] + nums[:i+1]
        if newnums == []:
            newnums = nums
        print(newnums)

        # 下面是手写的对分查找，似乎没有写好的可以用？
        i = 0
        j = len(newnums)-1
        while j >= i:
            k = (i+j)//2
            if newnums[k] == target:
                return True
            elif newnums[k] > target:
                j = k-1
            else:
                i = k + 1
        
        return False




# 遍历两次数组了，肯定有优化方法

s = Solution()
t = s.search([2],0)
print(t)