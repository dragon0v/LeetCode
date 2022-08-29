class Solution:
    def PredictTheWinner(self, nums) -> bool:
        # 递归
        # 玩家一得分取正，玩家二得分取负，看最后总分是正是负
        def total(start,end,turn):
            # turn表示玩家
            # 递归里并不需要显式定义分数变量
            if start==end:
                return nums[start]*turn
            scorestart = nums[start]*turn + total(start+1,end,-turn)
            scoreend = nums[end]*turn + total(start,end-1,-turn)
            return max(scorestart*turn,scoreend*turn)*turn # TODO 为啥这么多*turn
            # 这么多turn是因为这是在模拟玩家，双方都是最优策略
        
        return total(0,len(nums)-1,1)>=0 # 下标要-1