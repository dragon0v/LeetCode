# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        t = head
        l = 0
        while t!=None:
            l += 1
            t = t.next
        t = head
        for i in range((l)//2):
            t = t.next
        
        return t

# 两次遍历，第一次获得链表长度，第二次找到中间结点
