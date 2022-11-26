class Solution:
    def numberOfCuts(self, n: int) -> int:
        # 在这里错误解了，教训：一定要看看特殊值
        if n==1:
            return 0
        return n//2 if n%2==0 else n