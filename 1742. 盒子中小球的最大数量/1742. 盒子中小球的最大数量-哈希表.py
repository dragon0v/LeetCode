class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def getsum(x):
            # trick里的逐位求和算法
            return sum(map(int,str(x)))
        boxes = [0 for _ in range(50)]
        for ball in range(lowLimit,highLimit+1):
            boxes[getsum(ball)] += 1
        return max(boxes)