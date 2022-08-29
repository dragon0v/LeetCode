class Solution:
    def robot(self, command: str, obstacles, x, y):
        px = 0
        py = 0
        i = 0 # run i-th command
        while px <= x and py <= y:
            if command[i] == 'U':
                py += 1
            if command[i] == 'R':
                px += 1

            # if in 写法超时，对障碍物判断进行手写
            # 如果之后永远碰不到障碍物则将障碍物剔除列表
            # 依旧超时
            # 考虑对障碍数组进行预处理，成为三维数组，
            for o,ob in enumerate(obstacles):
                if ob[0] < px or ob[0] > x or ob[1] < py or ob[1] > y:
                    obstacles.pop(o)
                if ob == [px,py]:
                    return False



            if px==x and py==y:
                return True

            i = (i+1)%len(command)
        return False

# 超时