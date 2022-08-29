class Solution:
    def multiply(self, num1, num2):
        def c2d(c):
            #char to digit
            return ord(c)-ord('0')
        # num1 * num2 ，用num2的每一位乘num1再相加，每乘一次可以确定最后一位
        n1 = len(num1)
        n2 = len(num2)
        digits = [[0 for j in range(n2+n1-1)] for i in range(n2)] 
        # 存放每位相乘的中间结果
        # xxxx*xxx ,计算结果是7*3的矩阵
        # 每个元素可能是一位或者两位数
        for i in range(n2): #0,1,2
            for j in range(n1):#0,1,2,3
                digits[n2-i][j+n2-i] = c2d(num2[i])*c2d(num1[j])
        
        
        