# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        fast = head.next
        slow = head
        while fast!=None and slow!=None:
            if fast == slow:
                return True
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                fast = None
            if slow.next:
                slow = slow.next
            else:
                slow = None
        
        return False