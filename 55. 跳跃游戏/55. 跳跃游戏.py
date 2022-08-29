class Solution:
    def canJump(self, nums) -> bool:
        # 一开始想的bfs，但看数据量可能超时
        # 贪心？
        # 维护最远可以到达的距离，距离以下标计
        # 
        d = 0
        for i,v in enumerate(nums):
            if d<i:
                return False
            d = max(d,i+v)
        if d<i:
            return False
        return True