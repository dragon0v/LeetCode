class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # 能够原地修改是因为nums[i]在1-1000，而一个int的位数远超10，可以用高位储存结果
        # 时间为双倍
        for i in range(n):
            nums[2*i] |= (nums[i]&1023)<<12  # 10就行
            nums[2*i+1] |= (nums[i+n]&1023)<<12
        
        for i in range(2*n):
            nums[i] = nums[i]>>12
        
        return nums
