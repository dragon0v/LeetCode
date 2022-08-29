class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        t=date1.split("-")
        d1 = [int(t[0]),int(t[1]),int(t[2])]
        t=date2.split("-")
        d2 = [int(t[0]),int(t[1]),int(t[2])]
        
        # 不知道日期先后
        # 闰年判断
        
        if d1[0] > d2[0]:
            d1,d2 = d2,d1
        elif d1[0] == d2[0]:
            if d1[1] > d2[1]:
                pass
                