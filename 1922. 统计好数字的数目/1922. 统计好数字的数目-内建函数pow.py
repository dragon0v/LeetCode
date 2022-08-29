class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # 4位数，abcd，ac可以是02468，bd可以是2357
        # 5位数，abcde，ace可以是02468，bd可以是2357
        mask = 10**9+7
        odd = n//2
        even = n-odd
        '''
        pow内建函数
        pow(base: int, exp: int, mod: None = ...) -> Any
        pow(base: int, exp: int, mod: int) -> int
        pow(base: float, exp: float, mod: None = ...) -> float
        ...
        '''
        return pow(4,odd,mask)*pow(5,even,mask) % mask

s = Solution().countGoodNumbers(23000000000)
print(s)