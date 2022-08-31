from typing import *
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        # 4 pop 后能出的只有5或者3，
        a = popped[0]
        b = pushed.index(a)
        i,j = b-1,b+1
        
        for k in range(1,len(popped)):
            pop = popped[k]
            # if i>=0 and pop != pushed[i] and j<=len(pushed)-1 and pop!=pushed[j]:
            #     return False
            if i>=0 and pop == pushed[i]:
                i-=1
            elif j<=len(pushed)-1 and pop == pushed[j]:
                j+=1
            else:
                return False
        
        return True
# TODO [0,2,1],[0,1,2]
s = Solution().validateStackSequences([1,2,3,4,5],[4,5,3,1,2])
print(s)