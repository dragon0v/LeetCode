# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:48:11 2019

@author: NeoBanana
"""

#https://leetcode-cn.com/problems/prime-palindrome/
#866
'''
求出大于或等于 N 的最小回文素数。

回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。

例如，2，3，5，7，11 以及 13 是素数。

回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。

例如，12321 是回文数。

 

示例 1：

输入：6
输出：7
示例 2：

输入：8
输出：11
示例 3：

输入：13
输出：101
 

提示：

1 <= N <= 10^8
答案肯定存在，且小于 2 * 10^8。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prime-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
class Solution:
    def primePalindrome(self, N: int) -> int:
'''

class Solution:
    def primePalindrome(self, N: int) -> int:
        #思路：先判断有多少比n大的1、3、5、7、9开头的回文数，再判断回文数是否质数
        '''
        if N==1:
            return 2#要注意特殊情况呀
        '''
        if N<=2:
            return 2#wocaonima要注意特殊情况啊
        for i in range(N,200000001):
            
            l=len(str(i))
            if i//pow(10,l-1) in (1,3,5,7,9):
                if self.isPalindrome(i):
                    print(i)
                    if self.isPrime(i):
                        return i
                
        
    def isPrime(self,n:int):
        from math import sqrt
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
        return True
    def isPalindrome(self,n:int):
        s=str(n)
        for i in range(0,int((len(s)+1)/2)):
            #7,len=1 do=1
            #101,len=3 do=2
            #1001,len=4 do=2
            if s[i]!=s[-(i+1)]:
                return False
        return True
            
print(Solution().primePalindrome(9989900))
