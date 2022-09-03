from copy import deepcopy
from itertools import combinations
from typing import *
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        ans = 0
        def f(mat,mask):
            mat = deepcopy(mat)  # 不加会改原mat
            crt = 0
            for i in range(len(mat)):
                for m in mask:
                    mat[i][m] = 0
            
            for row in mat:
                if row==[0] * len(mat[0]):
                    crt += 1
            print(crt)
            return crt
        
        ans = max([f(mat,p) for p in combinations(range(len(mat[0])),cols)])
        return ans
