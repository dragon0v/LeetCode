import random
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        rx = ry = self.radius
        while rx**2+ry**2>=self.radius**2:
            # 可用random.uniform  x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            rx = (random.random()-0.5)*self.radius*2
            ry = (random.random()-0.5)*self.radius*2
            # print(rx,ry)
        return [self.x+rx,self.y+ry]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()