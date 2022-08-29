class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.medians = [] # 存放3个最中间的数
        self.nums = []
        self.l = 0 # nums 的长度

    def addNum(self, num):
        self.nums.append(num)
        self.nums.sort() # sort的内部实现方式是Timsort，如果输入已经有序，时间为O(N)
        self.l += 1


    def findMedian(self) -> float:
        if self.l%2 == 0:
            return (self.nums[self.l//2 - 1] + self.nums[self.l//2]) / 2
        return self.nums[self.l//2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()