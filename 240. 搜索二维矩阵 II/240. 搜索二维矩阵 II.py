class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 优化的方法是在对每行的搜索时采用对分查找
        for r in matrix:
            if r[0] == target or r[-1] == target:
                return True
            if r[0] < target and r[-1] > target:
                if target in r:
                    return True
            if r[0] > target:
                return False
            
        # 复杂度O(m)*O(n) = O(mn)
        