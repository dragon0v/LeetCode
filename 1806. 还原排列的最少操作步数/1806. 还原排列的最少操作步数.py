from copy import deepcopy


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # 直接模拟，主要涉及数组深浅复制
        # 1412ms，5%
        tar = [i for i in range(n)]
        perm = [i for i in range(n)]
        arr = [i for i in range(n)]
        tar = perm = [i for i in range(n)]
        for k in range(1,1010):
            for i in range(n):
                if i%2==0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n//2+(i-1)//2]
            perm = deepcopy(arr)
            if perm==tar:
                return k