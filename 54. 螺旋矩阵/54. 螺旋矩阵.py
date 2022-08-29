class Solution:
    def spiralOrder(self, matrix):
        # m * n
        self.mat = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.r1 = 0
        self.r2 = m - 1
        self.c1 = 0
        self.c2 = n - 1
        self.flag = True
        self.res = []
        def d1():
            for each in self.mat[self.r1][self.c1:self.c2+1]:
                self.res.append(each)
                self.r1 += 1
        def d2():
            for each in self.mat[self.c1:self.c2+1]:
                self.res.append(each)
        def d3():
            for each in self.mat[self.r2][self.c1:self.c2+1].reverse():
                self.res.append(each)
                self.r2 -= 1

        while(self.flag):
            d1()
            d2()
            d3()
            d4()