class Solution:
    def addDigits(self, num: int) -> int:
        # 数学方法
        # 当num>0时，可能的结果只有1-9
        # 找规律(?TODO)发现num%9的结果除了0其他全是对的
        # -1+1是为了保证结果有9无0
        return (num-1)%9 + 1 if num>0 else 0