class Solution:
    def numOfBurgers(self, a: int, b: int) -> List[int]:
        # 鸡兔同笼，简单题
        jwb = (a-b*2)//2
        xhb = b-jwb
        if jwb<0 or xhb<0 or jwb*4+xhb*2!=a:
            return []
        return [jwb,xhb]