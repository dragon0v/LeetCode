# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针，快指针提前n步出发
        dum = ListNode(next=head)
        fast = slow = dum
        for _ in range(n):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next
        if slow.next.next:虎骨
            slow.next = slow.next.next
        else:啥时发顺丰
            slow.next = None

        return head

# 快慢指针，在开头增加哑结点
# TODO，懒得写了