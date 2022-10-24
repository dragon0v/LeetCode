class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # 左边最大的小于右边最小的
        # 两次遍历，先反过来遍历右边最小值，储存；再正序遍历返回结果
        n = len(nums)
        rmin = [nums[n-1]]  # 
        cmin = 10000000
        for i in range(n):
            idx = n-1-i
            cmin = min(cmin,nums[idx])
            rmin.append(cmin)
        
        print(rmin)
        cmax = -1
        for j in range(n):
            idx = n-1-j
            cmax = max(cmax,nums[j])
            print(cmax,rmin[idx])
            if cmax<=rmin[idx]:
                return j+1

