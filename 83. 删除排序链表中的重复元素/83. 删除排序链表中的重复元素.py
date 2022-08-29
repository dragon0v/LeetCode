# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> ListNode:
        cur = head
        while cur:
            last = cur
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            last.next = cur.next
            cur = cur.next
        
        return head

            