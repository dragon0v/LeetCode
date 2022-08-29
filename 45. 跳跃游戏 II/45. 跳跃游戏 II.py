class Solution:
    def jump(self, nums) -> int:
        self.l = len(nums)
        self.jumps = 0
        self.found = False
        # dfs，但可能超时
        def dfs(pos,step):
            # 当前位于pos，向前进step步
            if pos + step > self.l-1:
                return
            elif pos + step == self.l-1:
                self.jumps += 1
                self.found = True
                return
            else:
                for i in range(step,1,-1):
                    dfs