class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # https://leetcode.cn/problems/cracking-the-safe/solutions/1349024/mei-tian-yi-dao-kun-nan-ti-di-61tian-po-xx8x3
        # 思路：如果达到理论最高压缩度，它的合并长度为k^n+n-1，
        # 枚举每一位，确保当前密码序列最后n位是一个新的密码
        # TODO why k^n+n-1?
        if n==1:
            return "".join(str(i) for i in range(k))
        self.ans = ""
        target = k**n+n-1  # 这个解法的关键在这，为什么是这个长度？
        S = set()  # 储存所有已枚举的后n位的值，即已枚举的密码
        def dfs(a):
            if len(a)==target:
                self.ans = a
                return
            o = a[-n+1:]  # 取a的后n-1位
            for i in range(k):
                s = o + str(i)  # 序列的后n位，即密码
                if s not in S:
                    # 理论最高压缩度时S中不应该出现重复值
                    S.add(s)
                    dfs(a+str(i))  # 当前的选择有戏，继续枚举下一位
                    S.remove(s)  # 跳出dfs说明当前的选择不对，回溯
                    if self.ans:  # 通过self实现很巧妙的退出条件，不加会枚举全部可行答案，显然超时
                        return 
                # else: 重复密码，直接pass

        dfs('')
        return self.ans

        # 还有一种特殊解法，官解的Hierholzer算法