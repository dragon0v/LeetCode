# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        ans = ListNode(0)
        t = ans
        # 这里是把相同长度的部分和超长部分分开
        # 也可以在循环中判断如果不够长了补0
        while l1 and l2:
            c, t.val = divmod(l1.val + l2.val + c, 10)
            l1 = l1.next
            l2 = l2.next
            if l1==None and l2==None:
                break
            else:
                t.next = ListNode(0)
                t = t.next
        while l1:
            c, t.val = divmod(l1.val + c, 10)
            l1 = l1.next
            if l1==None:
                break
            else:
                t.next = ListNode(0)
                t = t.next
        while l2:
            c, t.val = divmod(l2.val + c, 10)
            l2 = l2.next
            if l2==None:
                break
            else:
                t.next = ListNode(0)
                t = t.next

        if c==1:
            t.next = ListNode(c)


        return ans        

