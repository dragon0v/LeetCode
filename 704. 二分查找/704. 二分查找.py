class Solution:
    def search(self, num, target: int) -> int:
        i,j = 0,len(num)-1
        while i<=j:
            k = (i+j)//2
            if num[k] == target:
                return k
            elif num[k] > target:
                j = k - 1
            else:
                i = k + 1
        
        return -1