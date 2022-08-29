class Solution:
    def plusOne(self, digits):
        jinwei = 1
        n = len(digits)
        for i in range(n):
            if(jinwei!=1):
                break
            digits[n-i-1] += 1
            if(digits[n-i-1] == 10):
                jinwei = 1
                digits[n-i-1] = 0
            else:
                return digits
        #仍存在进位，说明位数+1，数组位数增加
        return [1] + [0 for i in range(n)]
s = Solution()
print(s.plusOne([9,9,6]))