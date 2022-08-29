# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:36:32 2021

@author: ToxicNeoBanana
"""

#978

class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        n = len(arr)
        maxLen = 1
        curLen = 1
        last = 0 #-1表示上一个符号是小于，1表示上一个符号是大于，0表示相等及重新开始
        for i in range(1,n-1):
            if(arr[i]<arr[i+1]):
                if(last == 1): #上一个是大于，子数组继续
                    curLen += 1
                    last = -1
                elif(last == -1): #上一个是小于，子数组终止
                    if (maxLen < curLen):
                        maxLen = curLen
                    curLen = 1
                    i -= 1
                    last = 0
                else: #上一个是0，重新开始
                    last = -1
            elif(arr[i]>arr[i+1]):
                if(last == -1): #上一个是小于，子数组继续
                    curLen += 1
                    last = 1
                elif(last == 1): #上一个是大于，子数组终止
                    if (maxLen < curLen):
                        maxLen = curLen
                    curLen = 1
                    i -= 1
                    last = 0
                else: #上一个是0，重新开始
                    last = 1
            else:#相等，子数组终止
                if (maxLen < curLen):
                    maxLen = curLen
                curLen = 1
                last = 0
                    
        return maxLen
        
    
arr = [9,4,2,10,7,8,8,1,9]
s = Solution().maxTurbulenceSize(arr)