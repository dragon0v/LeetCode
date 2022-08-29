# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2 == None:
            return l1
        i,j = l1,l2
        res = ListNode()
        k = res
        while i!=None and j!=None:
            print(i.val,j.val)
            if i.val <= j.val:
                k.next = i
                k = k.next
                i = i.next
            else:
                k.next = j
                k = k.next
                j = j.next
        
        if i:
            k.next = i
        else:
            k.next = j
        
        return res.next