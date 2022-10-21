class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 假设答案是1，推回去看第一个值是否等于0
        def dfs(r, c, cur):
            # row，column，当前对应回去的数
            if r == 1:
                return cur
            if (c % 2 == 0 and cur == 0) or (c % 2 == 1 and cur == 1):
                # 当前数是由1产生的情况：在偶数位的0 or 在奇数位的1
                return dfs(r - 1, (c - 1) // 2 + 1, 1)
            else:
                return dfs(r - 1, (c - 1) // 2 + 1, 0)
        
        # 假设答案是1，推回去发现确实是0，则返回1，否则说明答案应该是0
        return 1 if dfs(n, k, 1) == 0 else 0