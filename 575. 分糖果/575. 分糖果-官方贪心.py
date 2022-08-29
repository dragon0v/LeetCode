from typing import *
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # 糖果数量为n，妹妹最多拿到n/2种的糖果
        # 如果种类数m比n/2小，则只能拿到m种糖果；
        # 如果m比n/2大，但妹妹最多只能分到n/2个糖果，即n/2种
        return min(len(candyType)//2,len(set(candyType)))
s = Solution()
t = s.distributeCandies([1,1,1,2,3,1])
print(t)
