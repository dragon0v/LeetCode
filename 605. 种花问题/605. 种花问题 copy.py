class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        # 开头结尾连续两个0，或者中间连续三个0
        # 在开头结尾各补一个虚无的0，规律就一样了
        flowerbed = [1,0] + flowerbed + [0]
        print(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1 and flowerbed[i+1:i+4] == [0,0,0]:
                n-=1
                flowerbed[i+2] = 1
        return n <= 0
            

s = Solution()
t = s.canPlaceFlowers([0,0,1,0,1],1)
print(t)