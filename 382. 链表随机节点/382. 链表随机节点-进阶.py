import random
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 进阶：
    # 如果链表非常大且长度未知，该怎么处理？
    # 你能否在不使用额外空间的情况下解决此问题？
    
    # 特殊解法：水塘抽样
    # 核心思路：遍历链表到第i个元素时，它被选中的概率应该是1/i
    # 证明：如果i是最后一个元素，显然选中它的概率=1/n，符合题意
    # 如果i是倒数第二个元素，它被选中的概率是1/(n-1) * (n-1)/n = 1/n
    # 其他同理

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = 1
        ans = 0
        node = self.head
        while node:
            if random.randrange(i) == 0:
                # 每次有1/i的概率被选中
                ans = node.val
            i += 1
            node = node.next
        return ans




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()