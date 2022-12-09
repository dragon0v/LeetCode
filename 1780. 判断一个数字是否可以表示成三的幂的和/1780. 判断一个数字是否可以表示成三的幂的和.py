class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 思路：n的三进制中只可能有01，预处理的思路
        # 10^7以内的3的幂最大是3^16
        three_powers = [3**i for i in range(16,-1,-1)]
        for t in three_powers:
            d,n = divmod(n,t)
            print(d,n)
            if d==2:
                return False
        
        return True
