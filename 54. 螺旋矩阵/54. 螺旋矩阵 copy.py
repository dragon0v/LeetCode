class Solution:
    def spiralOrder(self, matrix):
        # m * n
        # [[1,2,3],[4,5,6],[7,8,9]]
        # return [1,2,3,6,9,8,7,4,5]
        
        res = []
        
        try:
            while 1:
                # 由左向右
                res += matrix[0]
                matrix.pop(0)
                # 由上到下
                for row in matrix:
                    res.append(row.pop(-1))
                # 由右向左
                t = matrix.pop(-1)
                t.reverse()
                res += t
                # 由下向上
                tt = []
                for row in matrix:
                    tt.append(row.pop(0))
                    tt.reverse()
                res += tt
        except:
            pass
            
        return res

# 和之前那个思路差不多，之前想太复杂了
# 这个try感觉很取巧，结束的判断应该也是挺重要的点
# 一种结束判断方式是输出矩阵的长度等于原矩阵就结束

r = Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(r)    