from copy import deepcopy


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # https://leetcode.cn/problems/minimum-number-of-operations-to-reinitialize-a-permutation/solutions/2052353/liang-chong-jie-fa-mo-ni-mo-ni-you-hua-b-2ijm/
        # 思路：无需模拟全部数字，通过观察发现此规则下所有数交换后形成若干个环，
        # 1或n-2必在最长的环中，且所有其他环的长度都是这个最长环长度的因数,
        # 因此模拟1或n-2进行交换的次数即可。
        # 模拟1交换的次数
        i = step = 1
        while 1:
            if i%2==0:
                i = i//2
            else:
                i = n//2 + (i-1)//2
            if i==1:
                return step
            step += 1