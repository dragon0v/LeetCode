class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 思路：n的三进制中只可能有01
        # 进制转换的模板代码
        while n>0:
            n,r = divmod(n,3)
            if r==2:
                return False
        
        return True
