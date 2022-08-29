class Solution:
    def reverseList(self, head):
        if head==None:
            return None
        # 思路是一次遍历，翻转箭头方向，返回最尾的指针
        pre = None
        while head != None: # 之前错在这里，写成了head.next这样最后一个节点就不被遍历了
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        return pre