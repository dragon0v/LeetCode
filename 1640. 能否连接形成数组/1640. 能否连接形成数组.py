from typing import *
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # 检查元素是否相同，其实不需要这步，在下面字典查找不存在则返回Flase即可
        p2 = []
        for p in pieces:
            for pp in p:
                p2.append(pp)
        
        p2.sort()
        p1 = sorted(arr)
        if p1!=p2:
            return False
        
        # 检查pieces中的元素是否在arr中顺序相同
        d = dict()
        for i,a in enumerate(arr):
            d[a] = i
        for p in pieces:
            idx = d[p[0]]
            if arr[idx:idx+len(p)] != p:
                return False
        
        return True