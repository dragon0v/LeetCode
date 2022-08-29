# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:26:31 2019

@author: NeoBanana
"""

#https://leetcode-cn.com/problems/day-of-the-week/

'''
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

 

示例 1：

输入：day = 31, month = 8, year = 2019
输出："Saturday"
示例 2：

输入：day = 18, month = 7, year = 1999
输出："Sunday"
示例 3：

输入：day = 15, month = 8, year = 1993
输出："Sunday"
 

提示：

给出的日期一定是在 1971 到 2100 年之间的有效日期。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-week
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
'''

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        #1970.1.1是星期四
        days=["Thursday", "Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday"]
        print(days[self.daysto1970(year,month,day)%7])
        return (days[self.daysto1970(year,month,day)%7])
    def daysto1970(self,year,month,day):
        days=0
        for i in range(1970,year):
            if self.isLeapyear(i):
                days+=366
            else:
                days+=365
        #print(days)
        
        non_leap=[31,28,31,30,31,30,31,31,30,31,30,31]
        leap=[31,29,31,30,31,30,31,31,30,31,30,31]
        for j in range(1,month):
            if self.isLeapyear(year):
                days+=leap[j-1]
            else:
                days+=non_leap[j-1]
        #print(days)
        
        days+=day-1
        #print(days)
        
        return days
        
    def isLeapyear(self,year):
        leap = False
        if year%4==0 and year%100!=0:
            leap = True
        if year%400==0:
            leap = True
        #print(leap)
        return leap
        
        
        
        
        
Solution().dayOfTheWeek(6,3,1995)
        
#PASSED 2019-9-17 20:06:32
        
#TODO 公式法？
        
        