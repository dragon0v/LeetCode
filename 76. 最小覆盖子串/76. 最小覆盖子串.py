class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Leetcode 101
        3.5滑动窗口
        思路是
        '''
        i,j = 0,0
        res = -1
        crt = 0
        pos = [0 for _ in range(128)] # 统计t中的字符数目
        flag = [False for _ in range(128)] # t中出现的字母
        for each in t:
            pos[ord(each)] += 1
            flag[ord(each)] = True

        for i,c in enumerate(s):
            if c in t:
                pos[i] = 1
        