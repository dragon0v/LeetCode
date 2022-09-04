from itertools import reduce
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (startPos-endPos+k) % 2!=0:
            return 0
        if k<abs(startPos-endPos):  # 第二个坑：
            return 0
        l = k-endPos+startPos
        # res = dp[end,0]=dp[end-1,1]+dp[end+1,1]
        # dp[x,j] = dp[x,j+2]+2
        
        # 在k次移动中要一共向右end-start步，则必发生(k-endPos+startPos)//2次left，k-left次right
        left = (k-endPos+startPos)//2
        if abs(startPos-endPos)==k:
            return 1
        # C(left,k)
        def C(a,k):
            if a==0:
                return 1
            up = reduce(lambda x,y:x*y,range(k, k-a,-1))
            down = reduce(lambda x,y:x*y,range(1,a+1))
            return up//down  # 第一个坑：大数使用int()会出错
        
        return C(left,k) % (10**9+7)
