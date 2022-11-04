class Solution:
    def reachNumber(self, target: int) -> int:
        # 从1到i，可以从中选若干个向右，其余向左
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        # 数学，此时target=0或负数，且其绝对值小于k，
        # 若tar=0则直接返回k，负数则需要将某些数变成负数，分情况讨论
        # 若tar为偶数，则必然可以找到一个偶数tar/2，将其取反便可以使数和为0，此时答案为k
        # 若tar为奇数，则先考虑k+1步，若此时tar为偶数，由上一步可知存在一个偶数tar/2；若k是偶数，则考虑k+2，此时必存在tar/2满足条件
        return k if target % 2 == 0 else k + 1 + k % 2

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/reach-a-number/solutions/1946020/dao-da-zhong-dian-shu-zi-by-leetcode-sol-ak90/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
