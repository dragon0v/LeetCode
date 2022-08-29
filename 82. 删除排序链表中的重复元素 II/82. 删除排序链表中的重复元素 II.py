# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> ListNode:
        # 扫一遍找重复
        # 再扫一遍删除
        dup = []
        last = None
        crt = head
        while crt:
            if last!=None and crt.val==last:
                dup.append(last)
            if crt.next == None:
                break
            last = crt.val
            crt = crt.next

        print(dup)

        last = None
        crt = head
        first = None #结果链表的头
        while crt:
            #print(crt.val)
            if crt.val not in dup:
                if last!=None:
                    last.next = crt
                last = crt
                if first == None:
                    first = crt
            else:
                if last!=None:
                    last.next = None
            if crt.next == None:
                break
            crt = crt.next

        return first
        
