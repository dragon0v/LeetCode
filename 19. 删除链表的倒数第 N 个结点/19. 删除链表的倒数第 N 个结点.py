# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针，快指针提前n步出发
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        # 对n=len的情况特殊考虑，直接返回头指针的下一个
        if fast != None:
            fast = fast.next
        else:
            return head.next
            
        while fast != None:
            fast = fast.next
            slow = slow.next
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head

# 快慢指针