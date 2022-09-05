from typing import *
import heapq

class SegmentTree:
    # https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/solution/xian-duan-shu-by-yyz561-p7d8/
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.avail = [True] * self.size * 2

    def update(self, idx, state):
        self.avail[idx] = state
        while idx >> 1:
            partner = idx - 1 if idx & 1 else idx + 1
            upper_state = self.avail[idx] | self.avail[partner]
            if not upper_state ^ self.avail[idx >> 1]:
                return
            self.update(idx >> 1, upper_state)

    def _find(self, idx):
        '''
        从中间节点往下寻找最左边的空闲节点（只有在中间节点显示范围内有空闲服务器才往下找）
        '''
        if idx >= self.size:
            return idx
        nxt = idx << 1
        if self.avail[nxt]:
            return self._find(nxt)
        else:
            return self._find(nxt+1)

    def _query(self, left, right):
        '''
        判断区间 [left, right] 是否存在空闲服务器
        '''
        if left == right:
            return left
        else:
            if left & 1:
                return left if self.avail[left] else self._query(left + 1, right)
            if not right & 1:
                prior = self._query(left, right - 1)
                return prior if self.avail[prior] else right
            return self._query(left >> 1, right >> 1)

    def query(self, idx):
        '''
        实现具体的搜索方法；优先右边最小，然后左边最小
        '''
        right_root = self._query(idx, self.size*2-1)
        if self.avail[right_root]:
            return self._find(right_root)
        elif idx > self.size:
            left_root = self._query(self.size, idx-1)
            if self.avail[left_root]:
                return self._find(left_root)
        return -1



class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 线段树 https://oi-wiki.org/ds/seg/
        # https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/solution/-by-hu-ge-8-k1o6/
        # 抄的https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/solution/xian-duan-shu-by-yyz561-p7d8/
        tree = SegmentTree(k)
        hp = []
        cnt = [0] * k
        for i in range(tree.size+k, tree.size << 1):
            tree.update(i, False)

        max_cnt = 0
        for idx, (at, lt) in enumerate(zip(arrival, load)):
            while hp and hp[0][0] <= at:
                tree.update(heapq.heappop(hp)[1]+tree.size, True)
            cur = tree.query(tree.size + idx % k)
            if cur != -1:
                cnt[cur-tree.size] += 1
                max_cnt = max(max_cnt, cnt[cur-tree.size])
                tree.update(cur, False)
                heapq.heappush(hp, (at+lt, cur-tree.size))

        return [i for i in range(k) if cnt[i] == max_cnt]


        