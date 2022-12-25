class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # 找连续的00两边是否一个1一个-1
        res = 0
        c0 = 0
        last = None
        for c in forts:
            if c==0:
                c0 += 1
            elif c==-1:
                if last==1:
                    res = max(res,c0)
                c0 = 0
                last = c
            else:
                if last == -1:
                    res = max(res,c0)
                c0 = 0
                last = c
        return res