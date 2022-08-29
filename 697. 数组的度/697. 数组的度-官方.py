class Solution:
    def findShortestSubArray(self, nums):
        mp = dict()

        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1 # num出现次数
                mp[num][2] = i # num最后出现位置
            else:
                mp[num] = [1, i, i] # _,num第一次出现位置,_
        
        maxNum = minLen = 0
        for count, left, right in mp.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                # 原答案elif内为：if minLen > (span := right - left + 1):
                    # := 海象表达式，Assignment Expression
                    # starting in Python 3.8, := is actually a valid operator that allows for assignment of variables within expressions 
                    # 用于在表达式中为变量赋值。 
                    # if (match := pattern.search(data)) is not None:
                    # Do something with match
                span = right - left + 1
                if(minLen > span):
                    minLen = span
        
        return minLen
    

# 思路：哈希表

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode-solution-ig97/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。