# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head==None:
            return head

        vals = []
        while head != None:
            vals.append(head.val)
            head = head.next
        
        n = len(vals)
        k = k % n

        last = None
        for i in range(len(vals)-1,-1,-1):
            cur = ListNode(vals[(i-k) % n],last)
            last = cur
        
        return last

# 耍赖方法，为了打卡，有时间在研究研究