class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums)<3:
            return False
        # 先顺序扫一遍数组，确定升序和降序的区间，ai总是选择升序的开始，aj总是选择升序的结束，ak为aj的下一个下降点
        ud = 1 # 储存升序降序，1升序0平-1降序
        last = nums[0]
        ai=[]
        ai.append(0)
        aj=[]
        ak=[]
        for i,each in enumerate(nums):
            if each > last : 
                if ud != 1: #升序的开始
                    ai.append(i)
                ud = 1
            elif each == last:
                ud = 0
            else:
                if ud != -1:
                    aj.append(i-1)
                    ak.append(i)
                ud = -1
            last = each
        print(ai,aj,ak)
        if not ai or not aj or not ak:
            return False
