class Solution:
    def robot(self, command: str, obstacles, x, y):
        # 这是看过题解的版本
        # 观察时间复杂度，x,y 都是上亿的，而command和obstacles都只有几千
        # 思路：指令循环会导致机器人位置的循环

        pass

s = Solution()
t = s.robot("URURRR",[[1,2],[3,4]],3,12)
print(t)