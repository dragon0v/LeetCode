import random
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 朴素思路：把链表转成list，随机返回
    # 感觉不是那么符合题意
    def __init__(self, head: Optional[ListNode]):
        self.l = []
        while head:
            self.l.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.l)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()