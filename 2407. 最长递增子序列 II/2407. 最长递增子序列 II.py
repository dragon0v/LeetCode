class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # 线段树+DP
        # TODO学习
        u = max(nums)
        mx = [0] * (4 * u)

        def modify(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m: modify(o * 2, l, m, i, val)
            else: modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R: return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m: res = query(o * 2, l, m, L, R)
            if R > m: res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii/solution/zhi-yu-xian-duan-shu-pythonjavacgo-by-en-p1gz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。