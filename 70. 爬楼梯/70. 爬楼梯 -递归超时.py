class Solution:
    def climbStairs(self, n: int) -> int:
        # 爬到第10层楼的所有方法为（从8楼爬2层+从9楼爬一层，注意8+1+1包含在9+1里面）
        def r(a):
            if a==1:
                return 1
            if a==2:
                return 2
            return r(a-1)+r(a-2)
        
        return r(n)