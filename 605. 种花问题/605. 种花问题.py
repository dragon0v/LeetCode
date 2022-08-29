class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        # 简单贪心，没必要看
        # 思路就是连着3个0，中间可以种花，种完变1，两边特殊考虑
        for i in range(0,len(flowerbed)):
            # 注意边界条件
            if (i==0 or flowerbed[i-1]==0) and flowerbed[i]==0 and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n -= 1
                flowerbed[i] = 1
        return n<=0

s = Solution()
t = s.canPlaceFlowers([0,0,1,0,1],1)
print(t)