# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
        # 双指针，每个指针遍历完这组遍历另一组
        pa = headA
        pb = headB
        while pa!=pb:
            # if pa!=None:
            #     pa = pa.next
            # else:
            #     # 不会存在第二次=None的情况，因为此时pa==pb
            #     pa = headB
            pa = pa.next if pa!=None else headB
            pb = pb.next if pb!=None else headA
            
        # 不太懂为什么这里return pa就行了
        # --在while外卖return是防止一开始就重合
        return pa