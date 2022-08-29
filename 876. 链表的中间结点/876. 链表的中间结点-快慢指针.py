# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = j = head
        while i != None and i.next != None:
            i = i.next.next
            j = j.next

        return j

# 快慢指针，i每次前进两步，j每次前进一步，i不能走了，j就在中间了
