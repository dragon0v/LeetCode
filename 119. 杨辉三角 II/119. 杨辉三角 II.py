class Solution:
    def getRow(self, rowIndex):
        rowIndex += 1
        if(rowIndex == 0):
            return []
        elif(rowIndex == 1):
            return [1]
        elif(rowIndex == 2):
            return [1,1]
        elif(rowIndex == 3):
            return [1,2,1]
        else:
            l = [0 for i in range(rowIndex)]
            l[0] = 1
            l[1] = 1
            for i in range(3, rowIndex+1):
                # 计算第i行的值
                #l[rowIndex] = 1
                l[rowIndex-1] = l[0] + l[1]
                for j in range(2,rowIndex):
                    l[0] = l[j-1] + l[j]
                    l[j-1] = l[rowIndex-1]
                    l[rowIndex-1] = l[0]
                l[0] = 1
                l[rowIndex-1] = 1
            return l

s = Solution()
print(s.getRow(5))
        